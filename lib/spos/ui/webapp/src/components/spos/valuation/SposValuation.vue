<template>
  <div>
    <v-card>
      <v-system-bar>
        <v-label>Valuation</v-label>
        <div class="my-2">
          <v-btn 
            v-show="editItem" 
            color="default" 
            fab x-small 
            @click="newItem()" >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>
        <v-spacer></v-spacer>
        <v-switch v-model="editItem"/>
      </v-system-bar>
      <v-card-title>Valuations</v-card-title>
      <v-card-text>
        <v-row align="center" style="height: 35px;" v-for="item in items" :key="item.id" >
            <v-label @click="setSelectedItem(item)">
              {{item.name}}
                <v-btn 
                  v-if="editItem" 
                  color="default" 
                  fab 
                  x-small
                  @click="setSelectedItem(item); dialog=true" >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
            </v-label>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- Dialog Valuation -->
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
                <v-chip x-small color="light green" fab text @click="newItem();dialog=false">ADD</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
                <v-chip x-small color="light red" fab text @click="deleteItem(selectedItem); dialog=false">DELETE</v-chip>
            </v-col>
            <v-col v-if="selectedItem != undefined">
              <v-chip x-small color="light orange" fab text @click="updateItem(selectedItem); dialog=false">UPDATE</v-chip> 
            </v-col>
            <v-col>
              <v-chip x-small color="light gray" fab text @click="setSelectedItem(undefined); dialog=false">CANCEL</v-chip> 
            </v-col>
          </v-row>
        </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import { mapActions, mapMutations, mapState, mapGetters } from 'vuex'

export default {
  name:"spos-valuation",
  computed: {
    ...mapState({
    }),
    ...mapGetters({
      items: "valuation/getValuations",
      selectedItem: "valuation/getSelectedValuation",
    }),
  },
  methods:{
    ...mapMutations({
      setSelectedItem: "valuation/setSelectedValuation"
    }),
    ...mapActions({
      newItem: "valuation/newValuation",
      updateItem: "valuation/updateValuation",
      deleteItem: "valuation/deleteValuation",
    }),
  },
  data () {
    return {
      dialog:false,
      editItem:false,
    }
  }
}
</script>