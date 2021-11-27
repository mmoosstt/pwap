<template>
  <v-card>
    <v-container>
      <!-- PDF
      <v-container>
        <v-btn x-small fab v-on:click="dialog = true"><v-icon>mdi-file-pdf</v-icon></v-btn>
      </v-container>
      -->
      <v-text-field dense filled outlined :label="$t('name')" v-model="pupilValuationSet.name" @change="changed(pupilValuationSet)"> </v-text-field>
      <v-row dense>
        <v-col><v-text-field dense filled outlined disabled :label="$t('changeDate')" v-model="pupilValuationSet.changeDate" /></v-col>
        <!--
        <v-col cols="1"><v-btn dense @click="dialog = true" color="light gray" small fab><v-icon>mdi-calendar</v-icon></v-btn></v-col>
        -->
      </v-row>
      <v-text-field dense filled outlined disabled :label="$t('id')" v-model="pupilValuationSet.id"> </v-text-field>
      <v-row dense v-for="pupilValuation in pupilValuationSet.children" :key="pupilValuation.id">
            <v-col><v-text-field dense filled outlined :label="$t(pupilValuation.name)" v-model="pupilValuation.gradeText"></v-text-field></v-col>
            <!-- <v-col><v-text-field dense v-model="pupilValuation.gradDescription"/></v-col>
            <v-col cols=9><v-slider dense v-model="pupilValuation.grad"  :tick-labels="['-1', '0', '1']" min="-1" max="1" ticks/></v-col>-->
      </v-row>
    </v-container>
    <v-dialog 
        v-model="dialog"
        persistent
        width="15cm"
      >
      <div>
        <v-card>
          <v-container>
            <v-row>
              <v-spacer></v-spacer>
              <v-btn icon color="black">
                <v-icon @click="dialog = false">mdi-close</v-icon>
              </v-btn>    
            </v-row>
          </v-container>   
        </v-card>
      </div>
        <v-card ref="foo" >
          <div v-if="pupil==undefined"/>
          <v-card-text v-else>
            <h1>{{pupil.givenName}} {{pupil.familyName}}</h1>
            <h2>Klasse: {{getSchoolClass(pupilValuationSet.id)}}</h2>
            <v-container dense v-for="pupilValuationSet in pupil.children" :key="pupilValuationSet.id">
              <h2>{{$t(pupilValuationSet.name)}}</h2>
              <h3>Datum: {{formatDate(pupilValuationSet.changeDate)}}</h3>
              <h3>Uhrzeit: {{formatTime(pupilValuationSet.changeDate)}}</h3>
              <h3>Durchschnitt: {{gradeMix(pupilValuationSet.children)}}</h3>
              <v-row dense v-for="pupilValuaton in pupilValuationSet.children" :key="pupilValuaton.id">
                  <v-card-text>
                    <h3>{{$t(pupilValuaton.name)}}</h3>
                    <p class="position:absolute; width: 100%;">{{pupilValuaton.gradeText}}</p>
                  </v-card-text> 
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
      </v-dialog>
  </v-card>
</template>


<script>
// import SposGrade from "./SposGrade";
// import moment from 'moment';
import { PupilValuationSetClient } from '../../../client/common'
// import jsPDF from 'jspdf' 

export default {
  name:"spos-school-pupil-valuation-set",
  components:{
   // "spos-grade": SposGrade
  },
  computed: {
    pupilValuationSet: {
        get: function () {
          return this.$store.getters['school/getSelectedItem'];
        },
        set: function (item) {
          this.$store.commit('school/setSelectedItem', item)
        }
      },
    pupil:{
      get: function(){
        return this.$store.getters['school/getPupil'](this.pupilValuationSet.id)
      }
    },
    changeDate:{
      get: function(){
        var date = this.pupilValuationSet.changeDate.toISOString().substr(0, 10)
        return date;
      },
      set: function(value){
        console.log(value);
      }
    },
      changeTime:{
      get: function(){
        var time = this.pupilValuationSet.changeDate.toISOString().substr(11, 8)
        return time ;
      },
      set: function(value){
        console.log(value);
      }
    },
  },
  methods:{
    getSchoolClass(pupilValuationSetId){
      return this.$store.getters["school/getSchoolClass"](pupilValuationSetId)
    },
    getPupil(pupilValuationSetId){
      return this.$store.getters["school/getSchoolClass"](pupilValuationSetId)
    },
    formatDate(date){
      var sdate=date.toISOString();
      var idate= sdate.slice(0,10);
      return idate;
    },
    formatTime(date){
      var sdate=date.toISOString();
      var itime= sdate.slice(11,16);
      return itime;
    },
    gradeMix(valuations){
      var sum = 0;
      var count = 0;
      for(var i in valuations){
        sum += valuations[i].grade;
        count += 1;
      }

      return (sum/count).toPrecision(3)
    },
    downloadServer(pupilId){
      var options_ = {
            method: "GET",
            headers: {
                "Accept": "application/doc"
            }
        };
      fetch(`http://localhost:8008/spos/report/pupil?pupilId=${pupilId}`, options_).then(response=>{
        return response.blob()}).then(myBlob=>{
          const url = window.URL.createObjectURL(myBlob)
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', `${pupilId}.docx`) //or any other extension
          document.body.appendChild(link)
          link.click()
        });
    },
    changed(pupilValuationSet){
      PupilValuationSetClient.pupilvaluationsetPut(pupilValuationSet)
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