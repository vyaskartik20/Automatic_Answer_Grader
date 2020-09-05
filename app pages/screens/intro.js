import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';

export default function Intro( {navigation} ) {

  const pressHandler = () => {
    navigation.push('Home')
  }

  return(

    <View style={styles.container}>
    <TouchableOpacity style={styles.romeo}
      onPress={pressHandler}
    >
        <Text  style={styles.colour}>
          Automatic Answer Grader
          {/* backgroundColor= "white" */}
        </Text>

        <View styles={styles.layer1}>
          <Text style={styles.italics}>
                evaluation simplified!
          </Text>
        </View>

        </TouchableOpacity>
      </View>  
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
  },
  colour: {
    // flex: 1,
    fontSize : 28,
    color: 'white',
    alignItems:'center',
    justifyContent: 'center',
  },
  layer1:{
    alignItems:'center',
    alignContent: 'center',
    justifyContent:'center'
  },
  italics:
  {
    fontFamily: 'italy-1',
    fontSize: 18,
    color:'teal',
    alignSelf:'flex-end',
    alignItems:'center',
    alignContent: 'center',
    justifyContent:'center'
  },
  romeo:
  {
    // alignItems: 'center',
    // alignContent: 'center',
    justifyContent: 'center',
    flex:1
  }
});