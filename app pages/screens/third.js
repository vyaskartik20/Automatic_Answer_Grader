import React, {useState} from 'react';
import { StyleSheet, Text, View, Image, ImageBackground, Button,TouchableOpacity, Modal } from 'react-native';
import {FontAwesome} from '@expo/vector-icons';
import * as ImagePicker from 'expo-image-picker';
// import axios from 'axios';
// import RNFetchBlob from 'react-native-fetch-blob'
 
// ../Grader_App/assets/back3.png
 
// const image = { uri: "https://reactjs.org/logo-og.png" };
export default function Third({navigation}) {
  // const [imageLoaded, setImageLoaded] = useState(false);
  const [open, setOpen] = useState(false);
  const [open2, setOpen2] = useState(true);


  const [t_attempted, setT_attempted]=useState(null);
  const [t_unattempted, setT_unattempted ]=useState(null);
  const [t_wrong, setT_wrong]=useState(null);
  const [t_score, setT_score]=useState(null);
  
  const pressHandler13 =() => {
    navigation.navigate('Picker3')
  }
 
  const pressHandler1 =() => {
    navigation.navigate('Capture3')
  }

  const pressHandler7 =() => {

    setOpen(false);
    // location=require('../assets/back3.jpg');
    // imagePath=null;
    navigation.navigate('Third',{
      // imagePath1: location1,
      // imagePath2: location2,
      imagePath: null
    })
  }


  const sendToServer= () => {

    let data = new FormData();
 
    console.log('NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
 
    const newFile = {
      uri: location2.uri, type: 'image/jpg',name : 'avatar1', filename :'imageName1.jpg'
    }
    data.append('files1', newFile)
    const newFile2 = {
      uri: location.uri, type: 'image/jpg' , name : 'avatar2', filename :'imageName2.jpg'
    }
    data.append('files2', newFile2)
    const newFile3 = {
      uri: location1.uri, type: 'image/jpg', name : 'avatar3', filename :'imageName3.jpg'
    }
    data.append('files3', newFile3)
 
    console.log(data)
 
 
 
    //working
 
    let baseURL='http://52.66.236.96:8080/';
    fetch( baseURL ,{ method: 'POST',headers:{  
        "Content-Type": "multipart/form-data",
        // "otherHeader": "foo",
        } , body :data} )
    .then((resp) => resp.json())    
    .then((respText) => {

      setT_attempted(JSON.parse(respText.attempted));
      setT_unattempted(JSON.parse(respText.unattempted));
      setT_wrong(JSON.parse(respText.wrong));
      setT_score(JSON.parse(respText.score));

      // setOpen2(false);
      setOpen(true);

      // alert('')

    })
    .catch((err) => {
      alert('Something went wrong. Kindly try again')
      // console.log();
    })



    // .then((respText) => {
    //   // console.log(resp);
    //   alert(JSON.stringify(respText));
    // })
 
    //
 
 
      //working
 
    // let baseURL='http://13.233.104.85:8080/';
    // axios.post(baseURL,data)
    // .then(function (response) {
    //   // console.log(response);
    //   console.log("response:    " +JSON.stringify(response));
    //   // alert('response');
    //   alert(JSON.stringify(response));
    // })
    // .catch(function (error) {
    //   console.log(error);
    //   alert(error);
    // });
 
    //
 
  }
 
  // var location= {require('../screens/back3.jpg')}
 
  var location1=navigation.getParam('imagePath1');
  var location2=navigation.getParam('imagePath2');
  var location=navigation.getParam('imagePath');
  return (
 
 
    <View style={styles.container}>
          <ImageBackground source={require('../assets/back3.jpg')} style={styles.background} >            
 
            <View style={styles.empty1}>
 
            </View>
 
            <View style={styles.button}>
              {/* <Button title="STUDENT'S RESPONSE" color="grey" /> */}
              <TouchableOpacity 
                style={styles.button3} 
                onPress={
                  // setImageLoaded(true)  
                  pressHandler13
                }
              >
                <Text style={{color: 'white',}}>STUDENT'S RESPONSE</Text>
              </TouchableOpacity>

              {/* <View style={styles.new}>
                <TouchableOpacity 
                  style={styles.button13} 
                  onPress={
                    pressHandler1
                  }
                >
                  <Text style={{color: 'white',}}>Take Picture</Text>
                </TouchableOpacity>
                <TouchableOpacity 
                  style={styles.button13}
                  onPress={
                    pressHandler13
                    // openImagePickerAsync
                    // location=setSelectedImage
                  }  
                >
                  <Text style={{color: 'white',}}>Select from Gallery</Text>
                </TouchableOpacity>
              </View> */}
            
            {/* {
              selectedImage &&

              {
                location=selectedImage
              }
            }  */}
 
              {
                location &&
                <Image
                  style={styles.tinyLogo}
                  source={location }
                />
              }
              
              {
                (!location) &&
                <Image
                  style={styles.tinyLogo}
                  source={require('../assets/back3.jpg')}
                /> 
              }
 
              
            </View>
 
            <TouchableOpacity 
              style={styles.button2} 
              onPress={sendToServer}
            >  
              <Text style={{color: 'white'}}>GET MARKS</Text>
            </TouchableOpacity>

            <View style={styles.matter} >
              <Text style={styles.matteri}>
                Processing may take upto a minute
              </Text>
            </View>

            <View style={styles.empty1}></View>

            {  
              open &&
              <Modal
                animationType="slide"
                transparent={false}
                visible={open}
              >
                <View style={{flex:1, backgroundColor: "white", justifyContent: 'center', alignItems: 'center'}}>
                  <View style={{
                    paddingVertical: 15,
                    paddingHorizontal: 10,
                    // flexDirection: "row",
                    justifyContent: "space-between",
                    alignItems: "center",
                  }}>
          
                    <Text style={styles.italics1}> TOTAL SCORE: {JSON.stringify(t_score)} / { parseInt(JSON.stringify(t_unattempted))+ parseInt(JSON.stringify(t_attempted))} {'\n'} </Text>
                    <Text style={styles.italics}>
                      Attempted Questions: {JSON.stringify(t_attempted)} {'\n'}
                      Unattempted Questions: {JSON.stringify(t_unattempted)} {'\n'}
                      Wrong Questions: {JSON.stringify(t_wrong)} {'\n'}
                    </Text>
                    

                    <View style={{color:'white'}}>
                      <TouchableOpacity style={styles.button4} onPress={pressHandler7} >
                        <Text style={{
                          color: 'black', 
                          fontFamily: 'nunito-regular',
                          fontSize: 22,
                          
                        }}>
                          Check for another student
                          </Text>
                      </TouchableOpacity>
                    </View>

                  </View>
                </View>
              </Modal>
            }


            

 
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
    flex:2.1
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
  button4: {
    height:"12%",
    color:'black',
    backgroundColor: 'teal',
    width:"100%",
    alignItems:'center',
    justifyContent: "center",
    padding:35,
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
  button13: {
    height:"10%",
    color:'white',
    backgroundColor: 'grey',
    width:"50%",
    alignItems:'center',
    justifyContent: "center",
    padding:5
  },
  new: {
    flexDirection:'row'
  },
  matter: {
    alignItems:'center'
  },  
  matteri:
  {
    fontFamily: 'nunito-regular',
    fontSize: 14,
    color:'rgb(41, 109, 255)',
    padding:10
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
    // backgroundColor:'white',
    // color:'blue'
    // alignItems:'space-between'
    // alignItems:'center',
    // justifyContent: "space-between"
  },
  italics:
  {
    fontFamily: 'nunito-bold',
    fontSize: 22,
    color:'teal',
    // alignSelf:'flex-end',
    alignItems:'center',
    alignContent: 'center',
    justifyContent:'center'
  },
  italics1:
  {
    fontFamily: 'nunito-regular',
    fontSize: 25,
    color:'teal',
    // alignSelf:'flex-end',
    alignItems:'center',
    alignContent: 'center',
    justifyContent:'center'
  },
});
 
 