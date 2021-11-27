<template>
  <v-card>
    <v-container>
      <v-text-field dense filled outlined disabled :label="$t('changeDate')" v-model="pupilValuation.changeDate"> </v-text-field>
      <v-text-field dense filled outlined disabled :label="$t('id')" v-model="pupilValuation.id"> </v-text-field>
    </v-container>
    <v-container dense>
     <v-row dense>
        <v-col cols=8><v-text-field dense filled outlined :label="$t('pupilValuation')" :value="pupilValuation.name" @change="changed(pupilValuation)"></v-text-field></v-col>
        <v-col cols=4><v-select return-object dense filled outlined v-model="selectedValuationDetail" item-text="grade" @changed="valuationDetailChanged()" :items="this.$store.getters['valuation/getValuationDetails'](pupilValuation.valuationId)" /></v-col>
    </v-row>
      <!--<v-row>
        <v-col cols=11><v-text-field dense v-model="pupilValuation.gradDescription"/></v-col>
        <v-col cols=1><v-btn x-small color="light green" fab v-on:click="addValuationDetailGradeText(pupilValuation.gradDescription)"><v-icon>mdi-plus</v-icon></v-btn></v-col>
      </v-row>-->
      <v-row dense>
        <v-col cols=11 dense>
          <v-combobox 
            return-object
            item-text="text"
            v-model="selectedValuationDetailText"
            v-bind:items="valuationDetailGradeTexts" 
            @change="addValuationDetailGradeText($event)"
            :label="$t('valuationText')" dense solo >
          </v-combobox>
        </v-col>
        <v-col cols=1><v-btn x-small color="light red" fab ><v-icon>mdi-minus</v-icon></v-btn></v-col>
      </v-row>
    </v-container>
  </v-card>
</template>


<script>
import { PupilValuationClient } from '../../../client/common'
export default {
  name:"spos-school-pupil-valuation",
  components:{
   // "spos-grade": SposGrade
  },
  mounted(){
    var i = this.$store.getters['valuation/getValuationDetails'](this.pupilValuation.valuationId);
    if(i.length>0){
      this.selectedValuationDetail = i[0];
    }
    else{
      this.selectedValuationDetail = undefined;
    }
    
    if (this.valuationDetailGradeTexts.length>0){
      this.selectedValuationDetailText = this.valuationDetailGradeTexts[0];
    }
    else{
      this.selectedValuationDetailText = undefined;
    }
    
  },
  methods:{
    changed(pupilValuation){
      PupilValuationClient.pupilvaluationPut(pupilValuation);
    },
    valuationDetailChanged(){
      if (this.valuationDetailGradeTexts.length>0){
        this.selectedValuationDetailText = this.valuationDetailGradeTexts[0];
      }
      this.selectedValuationDetailText=undefined;
    },
    getValuationDetailGradeText(){
      this.selectableGradeTexts =  this.$store.getters["valuation/getValuationDetailGradeText"](this.pupilValuation.valuationId, this.pupilValuation.grade);
      return this.selectableGradeTexts;
    },
    addValuationDetailGradeText(item){

      if (item.type === "valuationDetailText"){
        this.pupilValuation.grade = this.selectedValuationDetail.grade;
        this.pupilValuation.gradeText = item.text;
        this.$store.dispatch("school/updatePupilValuation2", this.pupilValuation);
      }
      else
      {
        if (item != ""){
          this.$store.dispatch("valuation/newValuationDetailText").then(newVDT=>{
            newVDT.text=item.trim();
            newVDT.valuationDetailId = this.selectedValuationDetail.id;
            newVDT.grade = this.selectedValuationDetail.grade;
            this.$store.dispatch("valuation/updateValuationDetailText", newVDT);
          });
          // PupilValuationClient.pupilvaluationPut(this.pupilValuation);
        }
      }
    }
  },
  computed: {
    pupilValuation: {
      get: function () {
        return this.$store.getters['school/getSelectedItem'];
      },
      set: function (item) {
        this.$store.commit('school/setSelectedItem', item)
      }
    },
    selectedValuationDetail: {
      get: function () {
        return this.selectedVD;
      },
      set: function (item) {
        this.selectedVD = item
      }
    },
    selectedValuationDetailText:{
      get: function () {
        return this.selectedVDT;
      },
      set: function (item) {
        this.selectedVDT = item
      }      
    },
    valuationDetailGradeTexts(){
      if (this.selectedValuationDetail != undefined){
        return  this.$store.getters["valuation/getValuationDetailTexts"](this.selectedValuationDetail.id);
      }
      return [];
    }
  },
  data () {
    return {
      selectableGradeTexts:[],
      selectedVD:undefined,
      selectedVDT:undefined,
      tickMin:0,
      tickMax:0,
    }
  }
}
</script>