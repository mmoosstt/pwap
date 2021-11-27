import Vue from "vue";
import Vuex from "vuex";
import { ValuationClient, ValuationDetailClient, ValuationDetailTextClient } from "../client/common"
import * as client from '../client/spos'

Vue.use(Vuex);

const state = {
  valuations: undefined,
  valuationDetails: undefined,
  valuationDetailTexts: undefined,
  selectedValuation: undefined,
  selectedValuationDetail: undefined,
  selectedValuationDetailText: undefined,
}

const getters = {
  getValuations(state) {
    return state.valuations;
  },
  getSelectedValuation(state) {
    return state.selectedValuation;
  },
  getSelectedValuationDetail(state) {
    return state.selectedValuationDetail;
  },
  getSelectedValuationDetailText(state) {
    return state.selectedValuationDetailText;
  },
  getValuationDetails: (state) => (valuationId) => {
    var result = [];
    for (var i in state.valuationDetails) {
      var valuationDetail = state.valuationDetails[i];
      if (valuationDetail.valuationId == valuationId) {
        result.push(valuationDetail);
      }
    }
    return result.sort((a, b) => {
      if (a.grade < b.grade) {
        return 1;
      }
      if (a.grade > b.grade) {
        return -1;
      }
      return 0;
    });
  },
  getValuationDetailTexts: (state) => (valuationDetailId) => {
    var result = [];
    for (var i in state.valuationDetailTexts) {
      var valuationDetailText = state.valuationDetailTexts[i];
      if (valuationDetailText.valuationDetailId == valuationDetailId) {
        result.push(valuationDetailText);
      }
    }
    return result;
  }
}

const mutations = {
  setSelectedValuation(state, items) {
    state.selectedValuation = items;
    state.selectedValuationDetail = undefined;
    state.selectedValuationDetailText = undefined;
  },
  setSelectedValuationDetail(state, items) {
    state.selectedValuationDetail = items;
    state.selectedValuationDetailText = undefined;
  },
  setSelectedValuationDetailText(state, items) {
    state.selectedValuationDetailText = items;
  },
  setValuations(state, items) {
    state.valuations = items;
  },
  setValuationDetails(state, items) {
    state.valuationDetails = items;
  },
  setValuationDetailTexts(state, items) {
    state.valuationDetailTexts = items;
  },
}
const actions = {
  update({ dispatch }) {
    dispatch("updateValuations");
    dispatch("updateValuationDetails");
    dispatch("updateValuationDetailTexts");
  },
  updateValuations({ commit }) {
    return new Promise((resolve)=>{  
      ValuationClient.all().then(v => {
        commit("setValuations", v.items);
        resolve(v.items);
      });
    });
  },
  newValuation({ dispatch }) {
    var item = new client.Valuation();
    item.name = "<new>"
    return new Promise((resolve)=>{ 
      ValuationClient.valuationPut(item).then((res) => {
        dispatch("updateValuations");
        resolve(res);
      });
    });
  },
  updateValuation({ dispatch }, item) {
    return new Promise((resolve)=>{
      ValuationClient.valuationPut(item).then((res) => {
        dispatch("updateValuations");
        resolve(res);
      });
    });
  },
  deleteValuation({ dispatch }, item) {
    return new Promise((resolve)=>{ 
      ValuationClient.valuationDelete(item.id).then((res) => {
        dispatch("updateValuations");
        resolve(res);
      });
    });
  },
  updateValuationDetails({ commit }) {
    return new Promise((resolve)=>{
      ValuationDetailClient.all().then(v => {
        commit("setValuationDetails", v.items);
        resolve(v);
      });
    });
  },
  newValuationDetail({ dispatch, getters }) {
    if (getters.getSelectedValuation != undefined) {
      var vdt = new client.ValuationDetail();
      vdt.valuationId = getters.getSelectedValuation.id;
      vdt.name = "<new>"
      return new Promise((resolve)=>{
          ValuationDetailClient.valuationdetailPut(vdt).then((res) => {
          dispatch("updateValuationDetails");
          resolve(res);
        });
      });
    }
  },
  updateValuationDetail({ dispatch }, item) {
    return new Promise((resolve)=>{ 
       ValuationDetailClient.valuationdetailPut(item).then((res) => {
        dispatch("updateValuationDetails");
        resolve(res);
      });
    });
  },
  deleteValuationDetail({ dispatch }, item) {
    return new Promise((resolve)=>{  
      ValuationDetailClient.valuationdetailDelete(item.id).then((res) => {
        dispatch("updateValuationDetails");
        resolve(res);
      });
    });
  },
  updateValuationDetailTexts({ commit }) {
    return new Promise((resolve)=>{  
      ValuationDetailTextClient.all().then(v => {
        commit("setValuationDetailTexts", v.items);
        resolve(v);
      });
    });
  },
  newValuationDetailText({ dispatch }) {
    var vdt = new client.Valuation();
    vdt.name = "<new>"
    return new Promise((resolve)=>{ 
      ValuationDetailTextClient.valuationdetailtextPut(vdt).then((res) => {
        dispatch("updateValuationDetailTexts");
        resolve(res);
      });
    });
  },
  updateValuationDetailText({ dispatch }, item) {
    return new Promise((resolve)=>{ 
      ValuationDetailTextClient.valuationdetailtextPut(item).then((res) => {
        dispatch("updateValuationDetailTexts");
        resolve(res);
      });
    });
  },
  deleteValuationDetailText({ dispatch }, item) {
    return new Promise((resolve)=>{
      ValuationDetailTextClient.valuationdetailtextDelete(item.id).then((result) => {
        dispatch("valuation/updateValuationTextDetails");
        resolve(result)
      });
    });
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}