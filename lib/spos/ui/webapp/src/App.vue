<template>
  <v-app color="blue-grey darken-1">
    <v-system-bar />
    <v-app-bar dark dense clipped max-height="50">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon @click="download()">mdi-filter</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute bottom temporary >
      <v-list nav dense>
        <v-list-item-group v-model="group">
          <v-list-item-title @click="selectView('school')">school</v-list-item-title>
          <v-list-item @click="callMe()">Add-School</v-list-item>
        </v-list-item-group>
        <v-list-item-group v-model="group">
          <v-list-item-title @click="selectView('valuation')">valuation</v-list-item-title>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-card extend>
      <spos-school-tree v-if="view ==='school'" ref="foo" />
      <spos-valuation-base v-else-if="view === 'valuation'" />
    </v-card>
  </v-app>
</template>

<script>
import SposSchoolTree from "./components/spos/school/SposSchoolTree"
import SposValuationBase from "./components/spos/valuation/SposValuationBase"

import jsPDF from 'jspdf' 
import html2canvas from "html2canvas"

export default {
  name: 'App',

  components: {  
    "spos-school-tree":SposSchoolTree,
    "spos-valuation-base":SposValuationBase,
  },
  created(){
    this.$store.dispatch("school/updateSchools")
    this.$store.dispatch("school/updateSchoolClasses")
    this.$store.dispatch("school/updatePupils")
    this.$store.dispatch("school/updatePupilValuations")
    this.$store.dispatch("school/updatePupilValuationSets")
    this.$store.dispatch("valuation/updateValuations")
    this.$store.dispatch("valuation/updateValuationDetails")
    this.$store.dispatch("valuation/updateValuationDetailTexts")
  },
  computed: {
    edit_mode: {
      get() {
        return this.$store.getters.get_edit_mode;
      },
      set(value) {
        this.$store.commit('set_edit_mode', value);
      },
    },
    group: {
      get() {
        return this.drawer;
      },
      set() {
        this.drawer = false;
      }
    }
  },
  methods:{
    selectView(view){
      console.log(view)
      this.$data.view = view;
    },
    download() {
    var pdf = new jsPDF();
    var element = this.$refs['foo'].$el;
    var width= element.style.width;
    var height = element.style.height;
    html2canvas(element).then(canvas => {
        var image = canvas.toDataURL('image/png');
        pdf.addImage(image, 'JPEG', 15, 40, width, height);
        pdf.save('facture' + '_' + new Date() + '.pdf');
    });
    },
    callMe(){
      console.log(this.$store.getters["getSchoolTree"])
      this.$store.dispatch("addSchool", {name: "School"}).then((school) => {
        console.log(school)
        this.$store.dispatch("addSchoolClass", {schoolId:school.id, name:"SchoolClass"}).then((schoolClass)=>{
          console.log(schoolClass)
          this.$store.dispatch("addPupil",{schoolClassId:schoolClass.id, givenName:"givenName", familyName:"familyName"}).then((pupil)=>{
            console.log(pupil)
            this.$store.dispatch("addPupilValuationSet", {pupilId:pupil.id}).then((pupilValuationSet)=>{
              console.log(pupilValuationSet)
            })
          })
        })
      });
    }
  },
  data: () => ({
      drawer: false,
      view:"school",
  })
}
</script>