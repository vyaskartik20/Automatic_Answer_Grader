


// import React, {useState} from 'react';
// import { StyleSheet, Text, View } from 'react-native';
// import * as Font from 'expo-font';
// import {AppLoading} from 'expo';
// import Intro from './screens/intro'
// // import Navigator from './routes/homeStack';

// const getFonts = () =>  Font.loadAsync({
//   'italic':require('./assets/fonts/ArchitectsDaughter-Regular.ttf')
// });


// export default function App() {
//   const [fontsLoaded, setFontsLoaded]= useState(false);
  
//   if(fontsLoaded)
//   {
//     return(
//       <Intro />
//     );
//   }
//   else{
//     return(
//       <AppLoading
//         startAsync={getFonts}
//         onFinsh={()=> setFontsLoaded(true)}
//       />
//     )
//   }
// }

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     backgroundColor: 'black',
// //     alignItems: 'center',
// //     justifyContent: 'center',
// //   },
// // });















import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
// import { Button, ThemeProvider } from 'react-native-elements';


export default function Intro() {
  return(
    <View style={styles.container}>
      <Text  style={styles.colour}>
        Automatic Answer Grader
        {/* backgroundColor= "white" */}
      </Text>
      <Text style={styles.italics}>
        evaluation simplified!
      </Text>
    </View>  
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },
  colour: {
    // flex: 1,
    fontSize : 28,
    color: 'white'
  },
  italics:
  {
    fontFamily: 'italic',
    fontSize: 18
  }
});













import React, {useState} from 'react';
import { StyleSheet, Text, View, Image, ImageBackground, Button,TouchableOpacity } from 'react-native';

// ../Grader_App/assets/back3.png

// const image = { uri: "https://reactjs.org/logo-og.png" };
export default function Second({navigation}) {

  const [imageLoaded, setImageLoaded] = useState(false);

  const pressHandler1 =() => {
    navigation.navigate('Capture3')
  }


  var location=navigation.getParam('imagePath');
  return (


    <View style={styles.container}>
          <ImageBackground source={require('../screens/back3.jpg')} style={styles.background} >            

            <View style={styles.empty1}>

            </View>

            <View style={styles.button}>
              {/* <Button title="STUDENT'S RESPONSE" color="grey" /> */}
              <TouchableOpacity 
                style={styles.button3} 
                onPress={
                  // setImageLoaded(true)  
                  pressHandler1
                }
              >
                <Text style={{color: 'white',}}>STUDENT'S RESPONSE</Text>
              </TouchableOpacity>
              
              {/* if(imageLoaded)
              {

              }
              else
              { */}
                <Image
                  style={styles.tinyLogo}
                  source={location}
                />
              {/* } */}
              
            </View>

            <TouchableOpacity style={styles.button2}>
              <Text style={{color: 'white'}}>GET MARKS</Text>
            </TouchableOpacity>
            {/* </View> */}

            {/* <View style={styles.button2}>
              <Button title="DONE" color="black" />
            </View> */}
            <View style={styles.empty1}></View>

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

  empty1:{
    flex:2
  },

  button: {
    flex:12,
    width: 400,
    height:"57%",
    // alignItems:'center',
    justifyContent: "space-between",
    padding: 50,
    // backgroundColor: 'grey'
  },
  button2: {
    height:"8%",
    color:'black',
    backgroundColor: 'teal',
    // width:"100%",
    alignItems:'center',
    justifyContent: "center",
    padding:25,
    // width:300
    // margin:55
  },
  button3: {
    height:"10%",
    color:'white',
    backgroundColor: 'grey',
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


























import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
// import { Button, ThemeProvider } from 'react-native-elements';


export default function App() {
  return(
    <View style={styles.container}>
      <Text  style={styles.colour}>
        Automatic Answer Grader
        {/* backgroundColor= "white" */}
      </Text>
      <View style={styles.italy}>
        <Text style={styles.colour2} >
          evaluation simplified!
        </Text>
      </View>  
    </View>  
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },
  colour: {
    // flex: 1,
    fontSize : 28,
    color: 'white'
  },
  colour2: {
    // flex: 1,
    fontSize : 18,
    color: 'pink'
  },
  italy: {
    fontFamily: "ArchitectsDaughter-Regular", 
    color: 'white',
    alignItems: 'flex-end',
    justifyContent: 'flex-end'
  }
});











