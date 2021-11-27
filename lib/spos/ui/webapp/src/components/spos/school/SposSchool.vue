<template>
  <v-card>
    <v-container fluid dense>
      <v-text-field dense filled outlined :label="$t('name')" v-model="school.name" @change="changed(school)"> </v-text-field>
      <v-text-field dense filled outlined disabled :label="$t('id')" v-model="school.id"> </v-text-field>
        <v-container>
            <v-btn x-small color="light green" fab v-on:click="addSchoolClass()"><v-icon>mdi-plus</v-icon></v-btn>
            {{$t('addSchoolClass')}}
        </v-container>
    </v-container>
  </v-card>
</template>


<script>
export default {
  name:"spos-school",
  computed: {
    school: {
    get: function () {
      return this.$store.getters['school/getSelectedItem'];
    },
    set: function (item) {
      this.$store.commit('school/setSelectedItem', item)
    },
  },
  },
  methods:{
    changed(school){
      this.$store.commit("addSchoolClass", school);
    },
    addSchoolClass(){
      this.$store.dispatch('school/addSchoolClass', {schoolId:this.school.id, name:"<insert-school-class-name>"});
      },
    getSchool(){
      this.$store.getSchool()
    }
  },
  data () {
      return {
        default:{schoolclass:{id:0,
                    name:"schoolclass",
                    type:"schoolclass",
                    children:[]}}
      }
  },
}
</script>