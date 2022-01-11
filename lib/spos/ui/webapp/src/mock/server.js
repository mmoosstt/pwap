import { Server, Model } from "miragejs"
var schoolData = {}

export function makeServer({ environment = "development" } = {}) {
  let server = new Server({
    environment,

    models: {
      pupil: Model,
    },

    seeds(server) {
      server.create("pupil", { givenName: "Bob", sureName:"BobO", id:1, type:"pupil"})
      server.create("pupil", { givenName: "Alice", sureName:"Alice=", id:2, type:"pupil"})
    },

    routes() {
      this.namespace = "v1"

      this.get("/spos/getPupil/:pupilId", (schema) => {
        return schema.pupil.all()
      }),

      this.get("/schools", () => {
          console.log("x")
        return schoolData
      })
    },
  })

  return server
}