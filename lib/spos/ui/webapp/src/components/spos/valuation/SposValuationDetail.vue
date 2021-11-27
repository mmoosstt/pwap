<template>
  <div>
    <v-card>
      <v-system-bar>
        <v-label>ValuationDetail</v-label>
        <div class="my-2">
          <v-btn 
            v-show="editItem" 
            color="default" 
            fab x-small 
            @click="cntrlValuationDetail('add')" >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
        <v-switch v-model="editItem"/>
      </v-system-bar>
      <v-card-title v-if="valuation!=undefined">{{valuation.name}}</v-card-title>
      <v-card-text v-if="valuation!=undefined">
        <v-list dense v-for="ValuationDetail in this.$store.getters['valuation/getValuationDetails'](valuation.id)" :key="ValuationDetail.id" >
          <v-row>
            <v-label 
              @click="selectValuationDetail(ValuationDetail)">
              {{ValuationDetail.name}} {{ValuationDetail.grade}}
              <v-btn 
                v-if="editItem" 
                color="default" 
                fab 
                x-small 
                
                @click="selectValuationDetailAndOpen(ValuationDetail)" >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
            </v-label>
          </v-row>
        </v-list>
      </v-card-text>
    </v-card>

    <!-- Dialog ValuationDetail -->
    <v-dialog v-model="dialog" persistent max-width="290" >
      <v-card>
        <v-card-title class="headline">
          <div v-if="selectedItem != undefined">{{selectedItem.type}}</div>
        </v-card-title>
        <v-list>
        <v-list-item v-if="selectedItem != undefined">
            <v-text-field label="name" v-model="selectedItem.name" />
        </v-list-item>
        <v-list-item v-if="selectedItem != undefined">
            <v-text-field label="grade" v-model="selectedItem.grade" />
        </v-list-item>
        <v-list-item>
          <v-row>
            <v-col v-if="selectedItem == undefined">
                <v-chip x-small color="light green" fab text @click="cntrlValuationDetail('add')">ADD</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
                <v-chip x-small color="light red" fab text @click="cntrlValuationDetail('delete', selectedItem)">DELETE</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
              <v-chip x-small color="light orange" fab text @click="cntrlValuationDetail('update', selectedItem)">UPDATE</v-chip> 
            </v-col>
            <v-col>
              <v-chip x-small color="light gray" fab text @click="cntrlValuationDetail('cancel')">CANCEL</v-chip> 
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
import { ValuationDetailClient } from '../../../client/common'

export default {
  name:"spos-valuation-detail",
  components:{
   // "spos-grade": SposGrade
  },
  computed: {
    valuation: function(){
      return this.$store.getters["valuation/getSelectedValuation"]
    },
    selectedItem: function(){
      return this.$store.getters["valuation/getSelectedValuationDetail"]
    },
  },
  created: function () {
   this.$store.dispatch("valuation/updateValuationDetails")
  },
  methods:{
    updateCntrl(){
      this.$store.dispatch("valuation/updateValuationDetails")
      this.$data.dialog = false;
      this.$data.selectedItem = undefined;
    },
    cntrlValuationDetail(action="add", vdt=undefined){
      if (action=="add"){
        var selValuation = this.$store.getters["valuation/getSelectedValuation"]
        if(selValuation.type==="valuation"){
          vdt = new client.ValuationDetail();
          vdt.valuationId = selValuation.id;
          vdt.name = "<new>"
          ValuationDetailClient.valuationdetailPut(vdt).then(()=>{
          this.updateCntrl()
        });
        }
      }
      else if (action=="update"){
        ValuationDetailClient.valuationdetailPut(vdt).then(()=>{
          this.updateCntrl()
        });
      }
      else if (action=="delete"){
        ValuationDetailClient.valuationdetailDelete(vdt.id).then(()=>{
          this.updateCntrl()
        });
      }
      else{
        this.updateCntrl();
      }
    },
    selectValuationDetail(item){
      this.$store.commit("valuation/setSelectedValuationDetail", item)
    },
    selectValuationDetailAndOpen(item){
      this.$store.commit("valuation/setSelectedValuationDetail", item)
      this.$data.dialog = true;
    },
    unselectValuationDetail(){
      this.$store.commit("valuation/setSelectedValuationDetail", undefined)
      this.$data.dialog = true;
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