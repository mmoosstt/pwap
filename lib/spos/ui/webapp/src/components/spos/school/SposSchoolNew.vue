<template>
  <v-card>
    <v-container fluid>
      <v-row dense>
        <v-card-title>
          <v-container>
            <v-row v-if="$store.getters.get_edit_mode" >
              <v-col>
                <v-text-field filled outlined :label="$t('name')" v-model="school.name" @change="changed(school)"> </v-text-field>
              </v-col>
            </v-row>
            <v-row v-else>
              <v-col>
                <v-text-field readonly outlined v-model="school.name"> </v-text-field>
              </v-col>
            </v-row>
              <v-container>
                  <v-row dense>
                  <v-col cols="auto">
                  <v-btn x-small color="light green" fab v-on:click="addSchoolMethode($item)"><v-icon>mdi-plus</v-icon></v-btn>
                  </v-col>
                  <v-col>
                  {{$t('addSchool')}}
                  </v-col>
                </v-row>
              </v-container>
              <div dense v-for="schoolclass in school.children" v-bind:key="schoolclass">
              <v-container v-if="schoolclass.children.length=='0'">
                <v-row dense >
                  <v-col cols="auto">
                  <v-btn x-small color="light red" fab v-on:click="removeSchool(schoolclass)"><v-icon>mdi-minus</v-icon></v-btn>
                  </v-col>
                  <v-col>
                  {{schoolclass.name}}
                  </v-col>
                </v-row>
              </v-container>
              </div>
            </v-container>
        </v-card-title>
      </v-row>
    </v-container>
  </v-card>
</template>


<script>
import { SchoolClient } from '../../../client/common'

export default {
  // name:"spos-new",
  computed: {
      school: {
      get: function () {
        return this.$store.getters['school/getSelectedItem'];
      },
      set: function (item) {
        this.$store.commit('school/setSelectedItem', item)
      }
    }
  },
  methods:{
    changed(school){
      SchoolClient.schoolPut(school);
    },
    addSchoolMethode(item){
      console.log("addSchoolMethode", item)
      this.$store.commit('set_id', this.$store.getters.get_id +1);
      this.$data.default.school.id = this.$store.getters.get_id;
      console.log("debug", this.$data.default.school);
      this.$store.dispatch("school/updateSchool", "new-school-added");
      },
    removeSchool(school)
    {
      this.$store.commit("remSchool", school)
    },
  },
  data () {
      return {
        default:{school:{id:0,
                    name:"newShool",
                    type:"school",
                    children:[]}}
      }
  },
}
</script>