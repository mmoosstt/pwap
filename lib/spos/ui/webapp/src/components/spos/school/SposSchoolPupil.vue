<template>
  <v-card>
    <v-container fluid dense>
      <v-text-field dense filled outlined :label="$t('givenName')" v-model="pupil.givenName" @change="changed(pupil)"> </v-text-field>
      <v-text-field dense filled outlined :label="$t('familyName')" v-model="pupil.familyName" @change="changed(pupil)"> </v-text-field>
      <v-text-field dense filled outlined disabled :label="$t('id')" v-model="pupil.id" @change="changed(pupil)"> </v-text-field>
        <v-container>
          <v-row>
            <v-btn x-small color="light green" fab v-on:click="addValuationSet()"><v-icon>mdi-plus</v-icon></v-btn>
            {{$t('addPupilValuationSet')}}
          </v-row>
          <v-row>
            <v-btn x-small fab v-on:click="downloadReport(pupil.id)">
              <v-icon>mdi-printer</v-icon>
            </v-btn>
          </v-row>
        </v-container>
    </v-container>
  </v-card>
</template>


<script>
import { PupilClient } from '../../../client/common'

export default {
  name:"spos-school-pupil",
  computed: {
      pupil: {
      get: function () {
        return this.$store.getters['school/getSelectedItem'];
      },
      set: function (item) {
        this.$store.commit('school/setSelectedItem', item)
      }
    }
  },
  methods:{
    changed(pupil){
      PupilClient.pupilPut(pupil);
    },
    addValuationSet(){
      this.$store.dispatch("school/addPupilValuationSet", {pupilId:this.pupil.id})
      },
    downloadReport(pupilId){
      var options_ = {
            method: "GET",
            headers: {
                "Accept": "application/doc"
            }
        };
      fetch(`/spos/report/pupil?pupilId=${pupilId}`, options_).then(response=>{
        return response.blob()}).then(myBlob=>{
          const url = window.URL.createObjectURL(myBlob)
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', `${pupilId}.docx`) //or any other extension
          document.body.appendChild(link)
          link.click()
        });
    },
  },
  data () {
    return {
      dialog:false,
      time:"",
      date:"",
    }
  }
}

</script>