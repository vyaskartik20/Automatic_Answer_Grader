import React, { useState, useEffect, useRef } from 'react';
import { Text, View, TouchableOpacity, Button, Image, SafeAreaView, Modal, StyleSheet } from 'react-native';
import { Camera } from 'expo-camera';
import {FontAwesome} from '@expo/vector-icons';

export default function Capture2({navigation}) {
  const camRef= useRef(null);
  const [hasPermission, setHasPermission] = useState(null);
  const [type, setType] = useState(Camera.Constants.Type.back);
  const [capturedPhoto, setCapturedPhoto] = useState(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  async function takePicture (){
    if (camRef) {
      const data = await camRef.current.takePictureAsync();
      setCapturedPhoto(data.uri);
      setOpen(true);
      // console.log(data);
    }
  }

  const returnBack = () =>{
    var imagePath= {uri: capturedPhoto}
    // navigation.navigate('Second', vSource);
    navigation.navigate('First', {
        // name: 'ImageEditor',
        // component: ImageEditor,
        imagePath2: imagePath,
    } )
  }

  return (

    <SafeAreaView style={{ flex: 1 , justifyContent:'center' }}>
      <Camera 
        style={{ flex: 1 }} 
        type={type}
        // ref={(ref: Camera) => {
        //   this.camera = this.snap;
        // }}
        ref={camRef}
      >
        <View
          style={{
            flex: 1,
            backgroundColor: 'transparent',
            flexDirection: 'row',
          }}>
          <TouchableOpacity
            style={{
              position:'absolute',
              flex: 0.1,
              alignSelf: 'flex-end',
              alignItems: 'center',
            }}
            onPress={() => {
              setType(
                type === Camera.Constants.Type.back
                  ? Camera.Constants.Type.front
                  : Camera.Constants.Type.back
              );
            }}>
            <Text style={{ fontSize: 18, marginBottom: 10, color: 'white' }}> Flip </Text>
          </TouchableOpacity>
        </View>
      </Camera>
        {/* <Button Title="Take Photo" onPress={this.snap} /> */}
      <TouchableOpacity style={styles.button} onPress={takePicture}  >
            <FontAwesome name="camera" size={23} color="#FFF"/>
      </TouchableOpacity>

      {
        capturedPhoto &&
        <Modal
          animationType="slide"
          transparent={false}
          visible={open}
        >
          <View style={{flex:1, justifyContent: 'center', alignItems: 'center', margin :20}}>

          <View style={{
            paddingVertical: 15,
            paddingHorizontal: 10,
            flexDirection: "row",
            justifyContent: "space-between",
            alignItems: "center"
            }}>
              <TouchableOpacity style={{margin:10}} onPress={()=> setOpen(false)}>
                <FontAwesome name="close" size={50} color="red" />
              </TouchableOpacity>
              <TouchableOpacity style={{margin:10}} onPress={()=> setOpen(returnBack)}>
                <FontAwesome name="check" size={50} color="red" />
              </TouchableOpacity>
            </View>  

            <Image
              style={{width:'100%', height:300 , borderRadius :20}}
              source={{uri: capturedPhoto}}
            />

          </View>
        </Modal>
      }

    </SafeAreaView>
  );
}

const styles= StyleSheet.create({
  button: {
    justifyContent:'center',
    alignItems: 'center',
    backgroundColor: '#121212',
    margin:20,
    borderRadius:10,
    height:50
  }
})



