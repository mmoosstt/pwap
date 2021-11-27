<template>
        <v-container fluid>
            <v-row>
                <v-col cols=5>
                    <v-card>
                        <v-treeview 
                        activatable 
                        return-object
                        @update:active="selectedItem($event)" 
                        :items="getSchoolTree">
                            <template v-slot:label="{ item }">
                                <div v-if="item == undefined"/>
                                <v-container v-else-if="item.type ==='pupil'">{{item.familyName}} {{item.givenName}}</v-container>
                                <v-container v-else-if="item.type ==='pupilValuation'">{{$t(item.name)}} {{item.grad}}</v-container>
                                <v-container v-else>{{$t(item.name)}}</v-container>
                            </template>
                            <template v-slot:prepend="{ item }">
                                <div v-if="item == undefined"/>
                                <v-btn v-else-if="item.type === 'school'" color="light gray" small fab><v-icon>mdi-bus-school</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'schoolClass'" color="light gray" small fab><v-icon>mdi-account-multiple</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'pupil'" color="light gray" small fab><v-icon>mdi-account</v-icon></v-btn>
                            </template>
                            <template v-slot:append="{ item }" >
                                <div v-if="item == undefined"/>
                                <v-btn v-else-if="item.type === 'school'" x-small color="light red" fab v-on:click="delSchool(item.id)"><v-icon>mdi-minus</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'schoolClass'" x-small color="light red" fab v-on:click="delSchoolClass(item.id)"><v-icon>mdi-minus</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'pupil'" x-small color="light red" fab v-on:click="delPupil(item.id)"><v-icon>mdi-minus</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'pupilValuationSet'" x-small color="light red" fab v-on:click="delPupilValuationSet(item.id)"><v-icon>mdi-minus</v-icon></v-btn>
                                <v-btn v-else-if="item.type === 'pupilValuation'" x-small color="light red" fab v-on:click="delValuation(item.id)"><v-icon>mdi-minus</v-icon></v-btn>
                            </template>
                        </v-treeview>
                    </v-card>
                </v-col>
                <v-col cols=7>
                    <div v-if="this.$store.getters['school/getSelectedItem'] == undefined" />
                    <spos-school v-else-if="this.$store.getters['school/getSelectedItem'].type === 'school'" />
                    <spos-school-class v-else-if="this.$store.getters['school/getSelectedItem'].type === 'schoolClass'" />
                    <spos-school-pupil v-else-if="this.$store.getters['school/getSelectedItem'].type === 'pupil'" />
                    <spos-school-pupil-valuation-set v-else-if="this.$store.getters['school/getSelectedItem'].type ==='pupilValuationSet'"/>
                    <spos-school-pupil-valuation v-else-if="this.$store.getters['school/getSelectedItem'].type ==='pupilValuation'"/>
                    <v-container v-else >
                        loading ...
                    </v-container>
                </v-col>
            </v-row>
            <v-row>
            </v-row>
        </v-container>
</template>


<script>

import SposSchoolPupil from "./SposSchoolPupil"
import SposSchool from "./SposSchool"
import SposSchoolClass from "./SposSchoolClass"
import SposSchoolPupilValuationSet from "./SposSchoolPupilValuationSet"
import SposSchoolPupilValuation from "./SposSchoolPupilValuation"


  //const con = require('electron').remote.getGlobal('console')
 // console.log('This will be output too the main process console.')
 
export default {
  name:"spos-school-tree",
  components:{
    "spos-school-pupil-valuation-set": SposSchoolPupilValuationSet,
    "spos-school-pupil-valuation": SposSchoolPupilValuation,
    "spos-school": SposSchool,
    "spos-school-class": SposSchoolClass,
    "spos-school-pupil": SposSchoolPupil,
  },
    computed:{
        getSchoolTree(){
            return this.$store.getters["school/getSchoolTree"];
        },
        /*
        selected: {
            get: function(){
                console.log("get", this.$data.sel)
                if (this.$data.sel == undefined){
                    return {type:null};
                }
                
                return this.$data.sel
            },
            set: function (value) {
                console.log("set", value)
                if (value == undefined){
                    this.$data.sel = {type:null};
                }
                else{
                    this.$data.sel = value;
                }
            }
        }*/
    },
    methods:{
        delSchool(Id){
            this.$store.commit("school/delSchool", Id);
        },
        delPupil(Id){
            this.$store.commit("school/delPupil", Id);
        },
        delSchoolClass(Id){
            this.$store.commit("school/delSchoolClass", Id);
        },
        delPupilValuationSet(Id){
            this.$store.commit("school/delPupilValuationSet", Id);
        },
        delValuation(Id){
            this.$store.commit("school/delValuation", Id);
        },
        selectedItem(item) {
            if (item !== undefined){
                return this.$store.commit("school/setSelectedItem", item[0]);
            }
            return this.$store.commit("school/setSelectedItem", undefined);
        },
    },
    data() {
        return {
            selected:{type:null},
            error:{}, 
        }
    }
}
</script>