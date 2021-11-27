<template>
  <v-card>
    <v-container fluid dense>
      <v-text-field dense filled outlined :label="$t('name')" v-model="schoolclass.name" @change="changed(schoolclass)"> </v-text-field>
      <v-text-field dense filled outlined disabled :label="$t('id')" v-model="schoolclass.id"> </v-text-field>
        <v-container>
          <v-row>
            <v-btn x-small color="light green" fab v-on:click="addPupil()"><v-icon>mdi-plus</v-icon></v-btn>
            {{$t('addPupil')}}
          </v-row>
         <v-row>
            <v-btn x-small fab v-on:click="downloadReport(schoolclass.id)">
              <v-icon>mdi-printer</v-icon>
            </v-btn>
          </v-row>
        </v-container>
    </v-container>
  </v-card>
</template>


<script>
// import SposGrade from "@/components/spos/SposGrade"
// import { SchoolClassClient } from '../../../client/common'

export default {
  name:"spos-school-class",
  components:{
    // "spos-grade": SposGrade
  },
  computed: {
    schoolclass: {
      get: function () {
        return this.$store.getters['school/getSelectedItem'];
      },
      set: function (item) {
        this.$store.commit('school/setSelectedItem', item)
      }
    }
  },
  methods:{
    changed(schoolclass){
      this.$store.commit("addSchoolClass", schoolclass)
    },
    addPupil(){
      this.$store.dispatch('school/addPupil', {schoolClassId:this.schoolclass.id, givenName:"<insert-pupil-givenName>", familyName:"<insert-pupil-familyName>"});
      },
    downloadReport(schoolClassId){
      var options_ = {
            method: "GET",
            headers: {
                "Accept": "application/doc"
            }
        };
      fetch(`/spos/report/schoolclass?schoolClassId=${schoolClassId}`, options_).then(response=>{
        return response.blob()}).then(myBlob=>{
          const url = window.URL.createObjectURL(myBlob)
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', `${schoolClassId}.docx`) //or any other extension
          document.body.appendChild(link)
          link.click()
        });
    },
  },
  data () {
    return {
      default:{
        pupil:{id:100,
          type:"pupil",
          familyName:"familyName",
          givenName:"givenName",
          children:[],
          }
        }
      }
    }
  }
</script>