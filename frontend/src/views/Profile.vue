<template>
  <div class="q-page flex flex-center q-my-md">
    <q-btn round>
      <q-avatar size="100px" color="primary" text-color="white">DT</q-avatar>
    </q-btn>
  </div>
  <div class="text-h4 text-weight-medium text-center">Duc Thanh Do</div>

  <q-tabs v-model="tab" class="bg-grey-12" dense align="justify"
    :style="{ marginLeft: '10%', marginRight: '10%', marginTop: '2%' }">
    <q-tab class="text-black" name="mails" label="Search Queries" />
    <q-tab class="text-black" name="alarms" label="Saved News" />
    <q-tab class="text-black" name="movies" label="Settings" />
  </q-tabs>

  <q-tab-panels v-model="tab" animated class="bg-grey-1" :style="{marginLeft: '10%', marginRight: '10%'}">
    <q-tab-panel name="mails">
      <q-badge v-for="x in 5" :key="x" class="q-mx-sm" :label="'Query ' + x" outline color="primary" @click="this.$router.push('/news')"/>
    </q-tab-panel>

    <q-tab-panel name="alarms">
      <div class="row">
          <NewsCard v-for="x in 4" :key="x" class="col" />
      </div>
    </q-tab-panel>

    <q-tab-panel name="movies">
      <div class="text-caption q-mb-sm">Password</div>
      <q-input outlined style="max-width: 600px" type="password" v-model="text" readonly dense></q-input>
      <div class="q-my-md q-gutter-sm">
        <q-btn outline color="primary" @click="newPassModal = true">Set New Password</q-btn>
        <q-btn color="negative" @click="deleteAccModal = true">Delete Account</q-btn>
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
            Are you sure to delete the account? (All saved news and information will be removed out of the system. This action is irreversible!)
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
            <q-input class="q-my-md" outlined style="max-width: 600px" type="password" v-model="text" dense></q-input>
            <div>Repeat New Password</div>
            <q-input class="q-my-md" outlined style="max-width: 600px" type="password" v-model="text" dense></q-input>
          </div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary">Cancel</q-btn>
          <q-btn v-close-popup flat color="primary" label="Change" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  
</template>
  
<script>
import { ref } from 'vue'
import { fabGithub } from '@quasar/extras/fontawesome-v6'
import NewsCard from '@/components/Card.vue'

const stringOptions = [
  'quasarframework/quasar',
  'quasarframework/quasar-awesome'
]

export default {
  name: 'MyLayout',
  components: {NewsCard},
  setup() {
    const text = ref('haha')
    const options = ref(null)
    const filteredOptions = ref([])
    const search = ref(null) // $refs.search
    const tab = ref('')
    const deleteAccModal = ref(false)
    const newPassModal = ref(false)

    function filter(val, update) {
      if (options.value === null) {
        // load data
        setTimeout(() => {
          options.value = stringOptions
          search.value.filter('')
        }, 2000)
        update()
        return
      }

      if (val === '') {
        update(() => {
          filteredOptions.value = options.value.map(op => ({ label: op }))
        })
        return
      }

      update(() => {
        filteredOptions.value = [
          {
            label: val,
            type: 'In this repository'
          },
          {
            label: val,
            type: 'All GitHub'
          },
          ...options.value
            .filter(op => op.toLowerCase().includes(val.toLowerCase()))
            .map(op => ({ label: op }))
        ]
      })
    }

    return {
      fabGithub,
      text,
      options,
      filteredOptions,
      search,
      filter,
      tab,
      deleteAccModal,
      newPassModal
    }
  }
}
</script>
