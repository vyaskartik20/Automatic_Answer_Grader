import React, {useState} from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View, ImageBackground, Button} from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function Picker3({navigation}) {
    let [selectedImage, setSelectedImage] = React.useState(null);

    const  pressHandler1 = () => {
        navigation.navigate('Capture3')
    }


    let openImagePickerAsync = async () => {
        let permissionResult = await ImagePicker.requestCameraRollPermissionsAsync();

        if (permissionResult.granted === false) {
            alert('Permission to access camera roll is required!');
            return;
        }
        
        let pickerResult = await ImagePicker.launchImageLibraryAsync();
        if (pickerResult.cancelled === true) {
                return;
        }
        setSelectedImage({ localUri: pickerResult.uri });
    };
        
    if (selectedImage !== null) {
        
        var imagePath= {uri: selectedImage.localUri}
        // navigation.navigate('Third', vSource);
        navigation.navigate('Third', {
                // name: 'ImageEditor',
            // component: ImageEditor,
            imagePath: imagePath,
        })
    }

    return(
        // {openImagePickerAsync}
        <View style={styles.container}>
          <ImageBackground source={require('../assets/back3.jpg')} style={styles.background} >
            
            <View style= {styles.last1}>
              <Text style={styles.italics} ></Text>
            </View>

            <View style={styles.matteri}>
              <Text style={styles.matteri}>
                Follow the instructions for best results
              </Text>
            </View>

            <View style= {{flex:0.1}}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>
            
            <View style={styles.button}>
              <Button 
              title="Take Photo " color="grey" 
              onPress={pressHandler1}
            />
            </View>
            
            <View style= {styles.last2}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>

            <View style={styles.button} color="grey">
              <Button 
                title="Upload Photo" 
                onPress={openImagePickerAsync}
                color="grey" 
              />
            </View> 

            <View style= {styles.last3}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>

          </ImageBackground>
        </View>  
    );
}
        
        
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: 'teal',
      // alignItems: 'center',
      // justifyContent: 'center',
    },
    button: {
      color: 'red',
      width: 320,
      justifyContent: "center",
      padding: 50,
      flex:1,
      // height:'40%'
  
    },
    last1:{
        flex:2
    },
    last2:{
        flex:0.1
    },
    last3:{
        flex:5
    },
    background: {
      flex: 1,
      resizeMode: "cover",
      justifyContent: "center",
      width: '100%'
    },
    italics:
    {
      fontFamily: 'nunito-regular',
      fontSize: 20,
      color:'teal',
    },
    matteri:
    {
      fontFamily: 'nunito-regular',
      fontSize: 17,
      color:'red',
      padding:10
    },
});

































// import React,  { Component} from 'react';
// import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
// import * as ImagePicker from 'expo-image-picker';

// class Picker3 extends Component {
// //   let [selectedImage, setSelectedImage] = React.useState(null);
// //   let [activate, setActivate] = useState(true);

//    openImagePickerAsync = async () => {
//     let permissionResult = await ImagePicker.requestCameraRollPermissionsAsync();

//     if (permissionResult.granted === false) {
//       alert('Permission to access camera roll is required!');
//       return;
//     }

//     let pickerResult = await ImagePicker.launchImageLibraryAsync();
//     if (pickerResult.cancelled === true) {
//       return;
//     }

//     selectedImage={ localUri: pickerResult.uri };



//     if (selectedImage !== null) {
//       // return (
//       //   <View style={styles.container}>
//       //     <Image source={{ uri: selectedImage.localUri }} style={styles.thumbnail} />
//       //   </View>
//       // );
  
//       var imagePath= { uri: selectedImage.localUri }
//       // navigation.navigate('Third', vSource);
//       navigation.navigate('Third', {
//           // name: 'ImageEditor',
//           // component: ImageEditor,
//           imagePath: imagePath,
//       } )
//     }
//   };


//   render()
  
// //   {openImagePickerAsync}
  
//   {
//     return (
//             // {openImagePickerAsync}
//             <View style={styles.container}>
//         <Image source={{ uri: 'https://i.imgur.com/TkIrScD.png' }} style={styles.logo} />
//         <Text style={styles.instructions}>
//             To share a photo from your phone with a friend, just press the button below!
//         </Text>

//         <TouchableOpacity onPress={openImagePickerAsync} style={styles.button}>
//             <Text style={styles.buttonText}>Pick a photo</Text>
//         </TouchableOpacity>
//         </View>


//     );
//   }
// }


// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   logo: {
//     width: 305,
//     height: 159,
//     marginBottom: 20,
//   },
//   instructions: {
//     color: '#888',
//     fontSize: 18,
//     marginHorizontal: 15,
//     marginBottom: 10,
//   },
//   button: {
//     backgroundColor: 'blue',
//     padding: 20,
//     borderRadius: 5,
//   },
//   buttonText: {
//     fontSize: 20,
//     color: '#fff',
//   },
//   thumbnail: {
//     width: 300,
//     height: 300,
//     resizeMode: 'contain',
//   }
// });


// export default Picker3;
// export default Picker3;