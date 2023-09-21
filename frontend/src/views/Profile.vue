<template>
  <div class="q-page flex flex-center q-my-md">
    <q-btn round>
      <q-avatar size="100px" color="primary" text-color="white">{{ user?.email[0] }}</q-avatar>
    </q-btn>
  </div>
  <div class="text-h4 text-weight-medium text-center">{{ user?.email }}</div>

  <q-tabs v-model="tab" class="bg-grey-12" dense align="justify"
    :style="{ marginLeft: '10%', marginRight: '10%', marginTop: '2%' }">
    <q-tab class="text-black" name="mails" label="Search Queries" />
    <q-tab class="text-black" name="alarms" label="Saved News" />
    <q-tab class="text-black" name="movies" label="Settings" />
  </q-tabs>

  <q-tab-panels v-model="tab" animated class="bg-grey-1" :style="{ marginLeft: '10%', marginRight: '10%' }">
    <q-tab-panel name="mails">
      <div v-if="!loadingQueries">
        <q-btn v-for="x in queries" :key="x.id" class="q-ma-md" :label="x.query" outline color="primary">
          <q-badge color="grey" floating @click="deleteQuery(x.query)">x</q-badge>
        



        



        </q-btn>
      </div>
      
        <div v-if="loadingQueries">
        <q-skeleton type="text" width="52%" class="text-subtitle1" />
        <q-skeleton type="text" width="52%" class="text-subtitle1" />
        <q-skeleton type="text" width="52%" class="text-subtitle1" />
      </div>
    </q-tab-panel>

    <q-tab-panel name="alarms">
      <div v-if="loadingNews">
        <q-card flat style="max-width: 300px">

<q-card-section>
  <q-skeleton type="text" class="text-subtitle1" />
  <q-skeleton type="text" width="50%" class="text-subtitle1" />
  <q-skeleton type="text" class="text-caption" />
</q-card-section>
</q-card>
      </div>
      <div v-if="!loadingNews">
        <NewsCard v-for="x in savedNews" :key="x.id" class="col" :news="x" />
      </div>
    </q-tab-panel>

    <q-tab-panel name="movies">
      <div>
        <div class="text-caption q-mb-sm">Password</div>
      <q-input outlined style="max-width: 600px" type="password" v-model="newPassword" readonly dense></q-input>
      <div class="q-my-md q-gutter-sm">
        <q-btn outline color="primary" @click="newPassModal = true">Set New Password</q-btn>
        <q-btn color="negative" @click="deleteAccModal = true">Delete Account</q-btn>
      </div>
      </div>
    </q-tab-panel>
  </q-tab-panels>

  <q-dialog v-model="deleteAccModal">
    <q-card class="my-card">
      <q-card-section>

        <div class="row no-wrap items-center">
          <div class="col text-h6 ellipsis">
            Delete Account?
          </div>
        </div>

      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="text-caption text-grey">
          Are you sure to delete the account? (All saved news and information will be removed out of the system. This
          action is irreversible!)
        </div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn v-close-popup flat label="Cancel"></q-btn>
        <q-btn v-close-popup flat color="primary" label="Confirm" />
      </q-card-actions>
    </q-card>
  </q-dialog>

  <q-dialog v-model="newPassModal">
    <q-card class="my-card" style="width: 600px">

      <q-card-section>

        <div class="row no-wrap items-center">
          <div class="col text-h6 ellipsis">
            Set new password
          </div>
        </div>

      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="text-caption text-grey">
          <div>Current Password</div>
          <q-input class="q-my-md" outlined style="max-width: 600px" type="password" v-model="text" dense></q-input>
          <div>New Password</div>
          <q-input v-model="formData.password" outlined dense type="password"
            error-message="At least 9 characters with A to Z, a to z, special character, 0 to 9"
            @change="validatePasswordActivities" :error="!validatePassword" />
          <div>Repeat New Password</div>
          <q-input v-model="formData.repeatPassword" type="password" outlined dense
            error-message="The repeat password should be the same as the password" :error="!validateRepeatPassword"
            @change="validateRepeatPasswordActivities" />
        </div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn v-close-popup flat color="primary">Cancel</q-btn>
        <q-btn v-close-popup flat color="primary" label="Change" @click="changePassword"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>
  
<script>
import { ref } from 'vue'
import NewsCard from '@/components/Card.vue'
import { validatePasswordMethod, validateRepeatPasswordMethod } from '@/utils/validation'
import {readUser} from '@/apis/users_api'
import {getQueries, readSavedNews, deleteQueryAPI} from '@/apis/news_api'

export default {
  name: 'MyLayout',
  components: { NewsCard },
  methods: {
    changePassword() {
      if (this.validatePassword
        && this.validateRepeatPassword
        && this.formData.password !== ''
        && this.formData.repeatPassword !== '') {

        console.log('OK')
        // /register API
      } else {
        console.log('Not OK')
      }
    },
    validatePasswordActivities() {
      this.validatePassword = this.validatePasswordMethod(this.formData.password)
    },
    validateRepeatPasswordActivities() {
      this.validateRepeatPassword = validateRepeatPasswordMethod(this.formData.password, this.formData.repeatPassword)
    },
    reloadingState() {
      setTimeout(() => {
         this.loadingQueries = false
       },1000);
    },
    async deleteQuery(query) {
      console.log('delete query ' + query)
      await this.deleteQueryAPI(query)
    }
  },
  async mounted() {
    this.user = await this.readUser('string')
    this.queries = await this.getQueries()
    this.savedNews = await this.readSavedNews()

    if(this.queries) {
      setTimeout(() => {
        this.loadingQueries = false
      },1000);
    }

    if(this.savedNews) {
      setTimeout(() => {
        this.loadingNews = false
      }, 1000)
    }
  },
  setup() {
    const newPassword = ref('anewpassword')
    const user = ref({
      email: ''
    })
    const search = ref(null) // $refs.search
    const tab = ref('')
    const deleteAccModal = ref(false)
    const newPassModal = ref(false)
    const validatePassword = ref(true)
    const validateRepeatPassword = ref(true)
    const formData = ref({
      password: '',
      repeatPassword: ''
    })

    const queries = ref([])
    const loadingQueries = ref(true)
    const loadingPassword = ref(true)

    const savedNews = ref([])
    const loadingNews = ref(true)

    return {
      newPassword,
      search,
      tab,
      formData,
      deleteAccModal,
      newPassModal,
      validatePassword,
      validateRepeatPassword,
      validatePasswordMethod,
      validateRepeatPasswordMethod,
      readUser,
      user,
      queries,
      getQueries,
      loadingQueries,
      loadingPassword,
      savedNews,
      loadingNews,
      readSavedNews,
      deleteQueryAPI
    }
  }
}
</script>
