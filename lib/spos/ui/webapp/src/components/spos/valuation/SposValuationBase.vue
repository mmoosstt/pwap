<template>
  <v-container>
    <v-row>
      <v-col>
        <spos-valuation />
      </v-col>
      <v-col>
        <spos-valuation-detail />
      </v-col>
      <v-col>
        <spos-valuation-detail-text />
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import * as client from '../../../client/spos'
import SposValuation from './SposValuation'
import SposValuationDetail from './SposValuationDetail'
import SposValuationDetailText from './SposValuationDetailText'
import { ValuationClient, ValuationDetailClient } from '../../../client/common'

export default {
  name:"spos-valuation-base",
  components:{
   "spos-valuation-detail-text": SposValuationDetailText,
   "spos-valuation-detail": SposValuationDetail,
   "spos-valuation": SposValuation,
  },
  created: function () {
   this.$store.dispatch("valuation/update")
  },
  computed:{
    test(){
      return this.$store.getters['valuation/getValuations'];
    }
  },
  methods:{
    selectValuation(item){
      this.$data.selValuation = item;
      this.$data.selValuationDetail = undefined;
    },
    delValuation(item){
      ValuationClient.valuationDelete(item.id);
      this.$store.dispatch("valuation/updateValuations");
      this.$data.dlgValuationDel = false;
    },
    delValuationDetail(item){
      ValuationDetailClient.valuationdetailDelete(item.id);
      this.$store.dispatch("valuation/updateValuationDetails");
      this.$data.dlgValuationDetailDel = false;
    },
    addValuation(){
      var v = new client.Valuation();
      ValuationClient.valuationPut(v);
      this.$store.dispatch("valuation/updateValuationDetails")
      this.$data.dlgValuation = false;
    },
    selectValuationDetail(item){
      console.log(item)
      this.$data.selValuationDetail = item;
    },
  },
  data () {
    return {
      dlgValuation:false,
      dlgValuationDel:false,
      selValuation:undefined,
      dlgValuationDetail:false,
      dlgValuationDetailDel:false,
      selValuationDetail:{},
    }
  }
}
</script>