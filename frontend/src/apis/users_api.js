import HTTP, {requestAPI} from './http_common'
import {return_authorization_header} from '@/utils/token'

export const readUser = async (email) => {
    try {
      const readUserPromise = HTTP.get("/users/" + email, {headers: return_authorization_header()})
      const data = await requestAPI(readUserPromise)
      return data
      
    } catch (error) {
      console.log(error);
      return error
    }
}





    // try {
    //   const eventsDynastyPromise = HTTP.get("/events/" + this.currentPage.dynasty)
    //   const eventsResult = await eventsDynastyPromise;

    //   const data = eventsResult.data
    //   this.contents_heads = Object.keys(data).reverse()
    //   this.events = Object.entries(data).reverse()
    //   this.events = this.events.map((event) => {
    //     return [event[0], event[1].reverse()]
    //   })
    // } catch (error) {
    //   console.log(error);
    // }
  


//   async getTimeline() {
//     try {
//       const eventsDynastyPromise = HTTP.get("/events/" + this.currentPage.dynasty)
//       const eventsResult = await eventsDynastyPromise;

//       const data = eventsResult.data
//       this.contents_heads = Object.keys(data).reverse()
//       this.events = Object.entries(data).reverse()
//       this.events = this.events.map((event) => {
//         return [event[0], event[1].reverse()]
//       })
//     } catch (error) {
//       console.log(error);
//     }
//   }

//   async getTimeline() {
//     try {
//       const eventsDynastyPromise = HTTP.get("/events/" + this.currentPage.dynasty)
//       const eventsResult = await eventsDynastyPromise;

//       const data = eventsResult.data
//       this.contents_heads = Object.keys(data).reverse()
//       this.events = Object.entries(data).reverse()
//       this.events = this.events.map((event) => {
//         return [event[0], event[1].reverse()]
//       })
//     } catch (error) {
//       console.log(error);
//     }
//   }

// async getTimeline() {
//     try {
//       const eventsDynastyPromise = HTTP.get("/events/" + this.currentPage.dynasty)
//       const eventsResult = await eventsDynastyPromise;

//       const data = eventsResult.data
//       this.contents_heads = Object.keys(data).reverse()
//       this.events = Object.entries(data).reverse()
//       this.events = this.events.map((event) => {
//         return [event[0], event[1].reverse()]
//       })
//     } catch (error) {
//       console.log(error);
//     }
// }