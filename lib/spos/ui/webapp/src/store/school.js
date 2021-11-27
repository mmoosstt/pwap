import Vue from "vue";
import Vuex from "vuex";
import * as client from "../client/spos";
import { v4 as uuidv4 } from 'uuid';
import * as api from '../client/common'



Vue.use(Vuex);

const state = {
    uid: 0,
    schools: [],
    schoolClasses: [],
    pupils: [],
    pupilValuationSets: [],
    pupilValuations: [],
    selectedItem:{},
}

const getters = {
    getSelectedItem: (state) =>{
        return state.selectedItem;
    },
    getPupil: (state) => (pupilValuationSetId) => {
        for (let i in state.pupilValuationSets) {
            var pupilValuationSet = state.pupilValuationSets[i];
            if (pupilValuationSet.id == pupilValuationSetId) {
                for (let ii in state.pupils) {
                    var pupil = state.pupils[ii];
                    if (pupil.id == pupilValuationSet.pupilId) {
                        return pupil;
                    }
                }
            }
        }
    },
    getSchoolClass: (state) => (pupilValuationSetId) => {
        for (let i in state.pupilValuationSets) {
            var pupilValuationSet = state.pupilValuationSets[i];
            if (pupilValuationSet.id == pupilValuationSetId) {
                for (let ii in state.pupils) {
                    var pupil = state.pupils[ii];
                    if (pupil.id == pupilValuationSet.pupilId) {
                        for (let iii in state.schoolClasses) {
                            var schoolClass = state.schoolClasses[iii];
                            if (schoolClass.id == pupil.schoolClassId)
                                return schoolClass.name;
                        }
                    }
                }
            }
        }
    },
    getValuationDetailGradeText: (state) => (valuationId, grade) => {
        for (let i in state.valuationDetails) {
            var valuationDetail = state.valuationDetails[i];
            if (valuationDetail.valuationId === valuationId && valuationDetail.grade === grade) {
                return valuationDetail.gradeTexts;
            }
        }
        return []
    },
    getSchoolTree(state) {
        state.schools.forEach(school => {
            Vue.set(school, "children", []);
            
            // schoolClasses
            state.schoolClasses.forEach(schoolClass => {
                if (schoolClass.schoolId == school.id) {
                    Vue.set(schoolClass, "children", []);
                    school.children.push(schoolClass)

                    // pupils
                    state.pupils.forEach(pupil => {
                        if (pupil.schoolClassId === schoolClass.id) {
                            Vue.set(pupil, "children", []);
                            schoolClass.children.push(pupil);

                            // pupilValuationSets
                            state.pupilValuationSets.forEach(pupilValuationSet => {
                                if (pupilValuationSet.pupilId === pupil.id) {
                                    Vue.set(pupilValuationSet, "children", []);
                                    pupil.children.push(pupilValuationSet)

                                    //pupilValuations
                                    state.pupilValuations.forEach(pupilValuation => {
                                        if (pupilValuation.pupilValuationSetId === pupilValuationSet.id) {

                                            // add grad descriptions of the same name
                                            for (let i in state.gradDescriptions) {
                                                let gradDescription = state.gradDescriptions[i];
                                                if (pupilValuation.name === gradDescription.valuationName) {
                                                    Vue.set(pupilValuation, "gradeDescriptions", gradDescription.descriptions);
                                                    break;
                                                }
                                            }
                                            pupilValuationSet.children.push(pupilValuation);
                                        }
                                    })
                                    pupilValuationSet.children = pupilValuationSet.children.sort((a, b) => (a.name > b.name) ? 1 : -1);
                                }
                            })
                        }
                    })
                }
            })
        });
        console.log(state)
        return state.schools;
    },
    getSchools({ state }) {
        return state.schools;
    },
    getSchoolClasses({ state }) {
        return state.schools;
    },
    getPupils({ state }) {
        return state.pupils;
    },
    getPupilValuationSets({ state }) {
        return state.pupilValuationSets;
    },
    getPupilValuations({ state }) {
        return state.pupilValuations;
    },
}

const mutations = {
    setSelectedItem(state, item){
        state.selectedItem = item;
    },
    addSchools(state, items) {
        state.schools = items;
    },
    addSchoolClasses(state, items) {
        state.schoolClasses = items;
    },
    addPupils(state, items) {
        state.pupils = items;
    },
    addPupilValuationSets(state, items) {
        state.pupilValuationSets = items;
    },
    addPupilValuations(state, items) {
        state.pupilValuations = items;
    },
}

const actions = {
    updateSchools({ commit }) {
        return api.SchoolClient.all().then(s => {
            commit("addSchools", s.items)
        });
    },
    updateSchoolClasses({ commit }) {
        return api.SchoolClassClient.all().then(s => {
            commit("addSchoolClasses", s.items)
        });
    },
    updatePupils({ commit }) {
        return api.PupilClient.all().then(s => {
            commit("addPupils", s.items)
        });
    },
    updatePupilValuationSets({ commit }) {
        return api.PupilValuationSetClient.all().then(s => {
            commit("addPupilValuationSets", s.items)
        });
    },
    updatePupilValuations({ commit }) {
        return api.PupilValuationClient.all().then(s => {
            commit("addPupilValuations", s.items)
        });
    },
    addValuationDetailText({ state }, { valuationId, grade, gradeText }) {
        return new Promise((resolve, reject) => {
            console.log({ valuationId, grade, gradeText })
            var found = false;
            console.log(state.valuationDetails)
            for (var i in state.valuationDetails) {
                console.log(state.valuationDetails[i])
                if (state.valuationDetails[i].valuationId === valuationId &&
                    state.valuationDetails[i].grade === grade) {
                    if (gradeText != null) {
                        state.valuationDetails[i].gradeTexts.unshift(gradeText);
                    }

                    var _vd = new client.ValuationDetail();
                    _vd.id = state.valuationDetails[i].id;
                    _vd.name = state.valuationDetails[i].name;
                    _vd.valuationId = valuationId;
                    _vd.grade = grade;
                    _vd.gradeTexts = state.valuationDetails[i].gradeTexts;
                    _vd.changeDate = new Date();

                    api.ValuationDetailClient.valuationdetailPut(_vd).then(valuationDetail => {
                        resolve(valuationDetail);
                    })
                    found = true;
                    break;
                }
            }
            if (!found) {
                reject("addValuationDetailText");
            }
        });
    },
    updateSchool({ dispatch }, { name }) {
        return new Promise(() => {
            var _school = new client.School();
            _school.id = uuidv4();
            _school.name = name;
            _school.changeDate = new Date();

            api.SchoolClient.schoolPut(_school).then(() => dispatch("updateSchools"));
        });
    },
    updateSchoolClass({ getters, dispatch }, { schoolId, name }) {
        return new Promise(() => {
            for (let i in getters.schools) {
                let _school = getters.schools[i];
                if (schoolId === _school.id) {
                    var _schoolClass = new client.SchoolClass();
                    _schoolClass.id = uuidv4();
                    _schoolClass.schoolId = schoolId;
                    _schoolClass.name = name
                    _schoolClass.changeDate = new Date();

                    api.SchoolClassClient.schoolclassPut(_schoolClass).then(() => dispatch("updateSchoolClasses"));
                }
            }
        });

    },
    updatePupil({ state }, { schoolClassId, familyName, givenName }) {
        return new Promise((resolve) => {
            for (let i in state.schoolClasses) {
                let _schoolClass = state.schoolClasses[i];
                if (schoolClassId === _schoolClass.id) {
                    var _pupil = new client.Pupil();
                    _pupil.id = uuidv4();
                    _pupil.schoolClassId = schoolClassId;
                    _pupil.givenName = givenName;
                    _pupil.familyName = familyName;
                    _pupil.changeDate = new Date();

                    api.PupilClient.pupilPut(_pupil).then(pupil => {
                        state.pupils.push(_pupil);
                        resolve(pupil);
                    });
                    break;
                }
            }
        });
    },
    updatePupilValuationSet({ getters, dispatch }, { pupilId }) {
        return new Promise((resolve) => {
            for (let i in getters.getPupils) {
                let _pupil = getters.getPupils[i];
                if (pupilId === _pupil.id) {
                    var _pvs = new client.PupilValuationSet()
                    _pvs.id = uuidv4();
                    _pvs.pupilId = pupilId;
                    _pvs.changeDate = new Date();
                    _pvs.name = "ValuationSet";

                    api.PupilValuationSetClient.pupilvaluationsetPut(_pvs).then(pupilValuationSet => {
                        dispatch("updatePupilValuationSets").then(() => {
                            api.ValuationClient.all().then(valuationSet => {
                                valuationSet.items.forEach(valuation => {
                                    var params = {
                                        pupilValuationSetId: pupilValuationSet.id,
                                        valuationId: valuation.id,
                                        name: valuation.name
                                    }
                                    dispatch("addPupilValuation", params);
                                });
                            })
                            resolve(pupilValuationSet)
                        });
                    });

                    break;
                }
            }
        });
    },
    updatePupilValuation2({dispatch}, pupilValuation){
        return new Promise((resolve)=>{
            api.PupilValuationClient.pupilvaluationPut(pupilValuation).then((res) => {
                dispatch("updatePupilValuations");
                resolve(res);
            });
        });
    },
    updatePupilValuation({ getters, dispatch }, { pupilValuationSetId, valuationId, name }) {
        return new Promise(() => {
            for (let i in getters.getPupilValuationSets) {
                let _valuationSet = getters.getPupilValuationSets[i];
                if (pupilValuationSetId === _valuationSet.id) {
                    var _pupilValuation = new client.PupilValuation();
                    _pupilValuation.id = uuidv4();
                    _pupilValuation.pupilValuationSetId = pupilValuationSetId;
                    _pupilValuation.valuationId = valuationId;
                    _pupilValuation.name = name;
                    _pupilValuation.changeDate = new Date();

                    api.PupilValuationClient.pupilvaluationPut(_pupilValuation).then(() => {
                        dispatch("updatePupilValuations");
                    });
                    break;
                }
            }
        });
    },
    updateValuation({ state, dispatch }, { name }) {
        return new Promise((resolve) => {
            for (let i in state.valuations) {
                let valuation = state.valuations[i];
                if (valuation.name === name) {
                    return resolve(valuation);
                }
            }
            var _valuation = new client.Valuation()
            _valuation.id = uuidv4();
            _valuation.name = name;
            _valuation.changeDate = new Date();

            api.ValuationClient.valuationPut(_valuation).then(valuation => {
                state.valuations.push(valuation);
                dispatch("addValuationDetail", { valuationId: valuation.id, grade: -1 });
                dispatch("addValuationDetail", { valuationId: valuation.id, grade: 0 });
                dispatch("addValuationDetail", { valuationId: valuation.id, grade: 1 });
                resolve(valuation);
            });

        });
    },
    updateValuationDetail({ state }, { valuationId, grade }) {
        return new Promise((resolve) => {
            for (var i in state.valuationDetails) {
                if (state.valuationDetails[i].id === valuationId) {
                    if (state.valuationDetails[i].grade === grade) {
                        // grade allready exists
                        resolve(state.valuationDetails[i]);
                        break;
                    }
                }
            }
            // add grade
            var _valuationDetail = new client.ValuationDetail()
            _valuationDetail.id = uuidv4();
            _valuationDetail.valuationId = valuationId;
            _valuationDetail.grade = grade;
            _valuationDetail.changeDate = new Date();

            api.ValuationDetailClient.valuationdetailPut(_valuationDetail).then(valuationDetail => {
                state.valuationDetails.push(valuationDetail);
                resolve(valuationDetail);
            });
        });
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}