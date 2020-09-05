import React from 'react';
import { StyleSheet, Text, View, Image, ImageBackground, Button,TouchableOpacity } from 'react-native';

// ../Grader_App/assets/back3.png

// const image = { uri: "https://reactjs.org/logo-og.png" };
export default function First({navigation}) {

  const  pressHandler1 = () => {
    navigation.navigate('Picker1')
  }

  const  pressHandler2 = () => {
    navigation.navigate('Picker2')
  }


  const  pressHandler3 = () => {
    navigation.navigate('Third',
    {
      imagePath1: location1,
      imagePath2: location2,
    })
  }

  // if(!location1)
  // {
    var location1=navigation.getParam('imagePath1');
  // }
  var location2=navigation.getParam('imagePath2');

  const image1 = { uri: "https://i2.wp.com/www.greaterkashmir.com/wp-content/uploads/2018/02/2018_2largeimg220_feb_2018_002638447.jpg?resize=480%2C320&ssl=1" };

  return (
    <View style={styles.container}>
          <ImageBackground source={require('../assets/back3.jpg')} style={styles.background} >

            <View style={styles.button}>
              <Button title="ANSWER KEY " onPress={pressHandler1} color="grey" />
            
            {
              (!location1) &&
              <Image
                style={styles.tinyLogo}
                source={require('../assets/back3.jpg')}
              />
            }     
            {
              (location1) &&
              <Image
                style={styles.tinyLogo}
                source={location1}
              />
            }     

            </View>

            

            <View style={styles.button}>
              <Button title="BLANK OMR" onPress={pressHandler2} color="grey" />

            {
              (!location2) &&
              <Image
                style={styles.tinyLogo}
                source={require('../assets/back3.jpg')}
              />
            }     
            {
              (location2) &&
              <Image
                style={styles.tinyLogo}
                source={location2}
              />
            }     
              
            </View>

            <TouchableOpacity style={styles.button2} onPress={pressHandler3}>
              <Text style={{color: 'white'}}>DONE</Text>
            </TouchableOpacity>

            {/* <View style={styles.button2}>
              <Button title="DONE" color="black" />
            </View> */}


          </ImageBackground>
      </View>  
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },


  button: {
    flex:5,
    width: 400,
    height:"47%",
    // alignItems:'center',
    justifyContent: "space-between",
    padding: 50

  },
  button2: {
    height:"6%",
    color:'white',
    backgroundColor: 'black',
    width:"100%",
    alignItems:'center',
    justifyContent: "center",
    padding:5
  },
  background: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center",
    width: '100%'
  },
  tinyLogo: {
    // flex:4,
    width:300,
    height:"75%",
    // margin:50, 
    padding:40,
    // backgroundColor:'black',
    // alignItems:'space-between'
    // alignItems:'center',
    // justifyContent: "space-between"
  },
});
