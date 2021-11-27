<template>
  <div>
    <v-card>
      <v-system-bar>
        <v-label>ValuationDetailText</v-label>
        <div class="my-2">
          <v-btn 
            v-show="editItem" 
            color="default" 
            fab x-small 
            @click="cntrlValuationDetailText('add')" >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
        <v-switch v-model="editItem"/>
      </v-system-bar>
      <v-card-title v-if="valuationDetail!=undefined">{{valuationDetail.grade}}</v-card-title>
      <v-card-text v-if="valuationDetail!=undefined">
        <v-list dense v-for="valuationDetailText in this.$store.getters['valuation/getValuationDetailTexts'](valuationDetail.id)" :key="valuationDetailText.id" >
          <v-row>
            <v-label
              @click="selectValuationDetailText(valuationDetailText)"
            >
              {{valuationDetailText.text}}
              <v-btn 
                v-if="editItem" 
                color="default" 
                fab 
                x-small  
                @click="selectValuationDetailTextAndOpen(valuationDetailText)">
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
            </v-label>
          </v-row>
        </v-list>
      </v-card-text>
    </v-card>

    <!-- Dialog ValuationDetailText -->
    <v-dialog v-model="dialog" persistent max-width="290" >
      <v-card>
        <v-card-title class="headline">
          <div v-if="selectedItem != undefined">{{selectedItem.type}}</div>
        </v-card-title>
        <v-list>
        <v-list-item v-if="selectedItem != undefined">
            <v-text-field label="text" v-model="selectedItem.text" />
        </v-list-item>
        <v-list-item>
          <v-row>
            <v-col v-if="selectedItem == undefined">
                <v-chip x-small color="light green" fab text @click="cntrlValuationDetailText('add')">ADD</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
                <v-chip x-small color="light red" fab text @click="cntrlValuationDetailText('delete', selectedItem)">DELETE</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
              <v-chip x-small color="light orange" fab text @click="cntrlValuationDetailText('update', selectedItem)">UPDATE</v-chip> 
            </v-col>
            <v-col>
              <v-chip x-small color="light gray" fab text @click="cntrlValuationDetailText('cancel')">CANCEL</v-chip> 
            </v-col>
          </v-row>
        </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import * as client from '../../../client/spos'
import { ValuationDetailTextClient } from '../../../client/common'

export default {
  name:"spos-valuation-detail-text",
  components:{
   // "spos-grade": SposGrade
  },
  computed:{
    valuationDetail: function(){
      return this.$store.getters["valuation/getSelectedValuationDetail"]
    },
    selectedItem: function(){
      return this.$store.getters["valuation/getSelectedValuationDetailText"]
    },
  },
  created: function () {
   this.$store.dispatch("valuation/updateValuationDetailTexts")
  },
  methods:{
    updateCntrl(){
      this.$store.dispatch("valuation/updateValuationDetailTexts")
      this.$data.dialog = false;
      this.$data.selectedItem = undefined;
    },
    cntrlValuationDetailText(action="add", vdt=undefined){
      console.log(this.valuationDetail)
      if (action=="add"){
        var selValuationDetail = this.$store.getters["valuation/getSelectedValuationDetail"]
        if(selValuationDetail.type==="valuationDetail"){
          vdt = new client.ValuationDetailText();
          vdt.valuationDetailId = selValuationDetail.id;
          vdt.text = "<new>"
          ValuationDetailTextClient.valuationdetailtextPut(vdt).then(()=>{
          this.updateCntrl()
        });
        }
      }
      else if (action=="update"){
        ValuationDetailTextClient.valuationdetailtextPut(vdt).then(()=>{
          this.updateCntrl()
        });
      }
      else if (action=="delete"){
        ValuationDetailTextClient.valuationdetailtextDelete(vdt.id).then(()=>{
          this.updateCntrl()
        });
      }
      else{
        this.updateCntrl()
      }
    },
    selectValuationDetailTextAndOpen(item){
      this.$store.commit("valuation/setSelectedValuationDetailText", item)
      this.$data.dialog = true;
    },
    selectValuationDetailText(item){
      this.$store.commit("valuation/setSelectedValuationDetailText", item)
    },
    unselectValuationDetailText(){
      this.$store.commit("valuation/setSelectedValuationDetailText", undefined)
      this.$data.dialog = false;
    }
  },
  data () {
    return {
      dialog:false, 
      editItem:false,
    }
  }
}
</script>