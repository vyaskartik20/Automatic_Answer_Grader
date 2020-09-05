'use strict';
 
import React, {Component} from 'react';
import GestureRecognizer, {swipeDirections} from 'react-native-swipe-gestures';
import { StyleSheet, Text, View, Image, ImageBackground, Button, TouchableOpacity, ScrollView } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import {FontAwesome} from '@expo/vector-icons';
 
class SomeComponent extends Component {
 
  constructor(props) {
    super(props);
    this.state = {
      myText: 'I\'m ready to get swiped!',
      gestureName: 'none',
      backgroundColor: '#fff'
    };
  }
 
  onSwipeUp(gestureState) {
    this.setState({myText: 'You swiped up!'});
  }
 
  onSwipeDown(gestureState) {
    this.setState({myText: 'You swiped down!'});
  }
 
  onSwipeLeft(gestureState) {
    this.setState({myText: 'You swiped left!'});
    
  }
 
  onSwipeRight(gestureState) {
    this.setState({myText: 'You swiped right!'});
    this.props.navigation.push('Home')
  }

  pressHandler1 = (gestureState) => {
    this.props.navigation.push('Download')
  }

  pressHandler2 = (gestureState) => {
    this.props.navigation.push('First')
  }
 
  onSwipe(gestureName, gestureState) {
    const {SWIPE_UP, SWIPE_DOWN, SWIPE_LEFT, SWIPE_RIGHT} = swipeDirections;
    this.setState({gestureName: gestureName});
    switch (gestureName) {
      case SWIPE_UP:
        {
          this.setState({backgroundColor: 'red'});
          break;
        }
      case SWIPE_DOWN:
        this.setState({backgroundColor: 'green'});
        break;
      case SWIPE_LEFT:
        this.setState({backgroundColor: 'blue'});
        break;
      case SWIPE_RIGHT:
        this.setState({backgroundColor: 'yellow'});
        break;
    }
  }
 
  render() {
 
    const config = {
      velocityThreshold: 0.3,
      directionalOffsetThreshold: 80
    };
 
    return (
      <GestureRecognizer
        onSwipe={(direction, state) => this.onSwipe(direction, state)}
        onSwipeUp={(state) => this.onSwipeUp(state)}
        onSwipeDown={(state) => this.onSwipeDown(state)}
        onSwipeLeft={(state) => this.onSwipeLeft(state)}
        onSwipeRight={(state) => this.onSwipeRight(state)}
        config={config}
        style={{
          flex: 1,
          backgroundColor: this.state.backgroundColor
        }}
        >
        {/* <Text>{this.state.myText}</Text>
        <Text>onSwipe callback received gesture: {this.state.gestureName}</Text> */}
      
        <ScrollView style={styles.container}>
          {/* <ImageBackground source={require('../screens/back3.jpg')} style={styles.background} > */}
  

            <View style= {styles.last}>
              <Text style={styles.italics} >Swipe right to go back </Text>
              <FontAwesome name="angle-right" size={28} color="teal" />
              <FontAwesome name="angle-right" size={28} color="teal" />
              <FontAwesome name="angle-right" size={28} color="teal" />
            </View>

            <View>

                <Text style={styles.head}>INSTRUCTIONS</Text>

              <View style={{margin:10, flexDirection:'row'}} >
                <FontAwesome name="angle-right" size={28} color="teal" />
                <Text style={styles.matteri}>
                   Take the photo in considerable amount of light
                </Text>
              </View>

              <View style={{margin:10, flexDirection:'row'}} >
                <FontAwesome name="angle-right" size={28} color="teal" />
                <Text style={styles.matteri}>
                   The photo should not have any shadow, position your hands accordingly while taking the photo
                </Text>
              </View>

              <View style={{margin:10, flexDirection:'row'}} >
                <FontAwesome name="angle-right" size={28} color="teal" />
                <Text style={styles.matteri}>
                   The photo of the OMR should be verically upside down; tilting or photos at an angle 
                   would not be a problem, howewer. Photos in horizontal orientation of the OMR should not be used.
                </Text>
              </View>

              <View style={{margin:10, flexDirection:'row'}} >
                <FontAwesome name="angle-right" size={28} color="teal" />
                <Text style={styles.matteri}>
                  After sending a request of getting marks, a data transfer of roughly 10 to 15 mbs will take place. So be patient
                  according to your network connection. A good network connection is preferred.
                </Text>
              </View>




                <Text style={styles.matter}>
                    This app is made for the purpose of making the evaluation process easier to assist the instructors
                    in auto grading answer sheets and saving their valuable time. This app can be 
                    easily used for grading an OMR test based examination of hundreds or thousands of students.
                </Text>

                <Text style={styles.matter}>
                    Three images are needed to be uploaded.
                    First, the answer key ;
                    Second, the blank OMR sheet that is used for examination and ; 
                    Third, the student's response that is to be evaluated.
                </Text>

                <Text style={styles.matter}>
                    It is recommended to use the OMRs provided in the app. Though any OMR sheet which contains the questions
                    inside rectangular boxes (like the provided OMRs) can be graded accuarately. We have tested the app thoroughly
                    and we sincerely hope that this app can be of good use to you.
                </Text> 

            </View>

            <View>

                <Text style={styles.head}>ABOUT US</Text>

                <Text style={styles.matter}>
                    We are thankful to our instructor, Dr. Anand Mishra, Assistant Professor at IIT Jodhpur, for providing us the necessary guidance, without which this 
                    app could not have been completed.
                </Text>

                <Text style={styles.matter}>
                     Also, we would like to thank Abhirama Subramanyam Penamakuri, a PhD student at IIT-J, 
                     for his much needed support and helping us throughout the course of the project.
                </Text>      
                <Text style={styles.matter}>
                    Currently, we are two B-Tech students here, at IIT-J, Aditya 
                    Kumar and Kartik Vyas, interested in good and new technology with an aim to learn the things that make life easier
                    for people. This app uses image-processing algorithms for auto grading of answer sheets. This app is built 
                    in react native.  
                </Text>
            
            </View>

          {/* </ImageBackground> */}
        </ScrollView>  



      
      
      
      </GestureRecognizer>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'rgb(230, 239, 255)',
    // backgroundColor: 'rgb(255, 220, 220)',
    // alignItems: 'center',
    // justifyContent: 'center',
  },
  background: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "flex-start",
    width: '100%'
  },
  italics:
  {
    fontFamily: 'nunito-regular',
    fontSize: 20,
    color:'teal',
  },
  last : {
    alignSelf:'flex-start',
    alignItems:'flex-start',
    justifyContent: 'flex-start',
    padding:15,
    marginTop: 30,
    flexDirection:'row'
  },
  matter:
  {
    fontFamily: 'nunito-regular',
    fontSize: 17,
    color:'teal',
    padding:10
  },
  matteri:
  {
    fontFamily: 'nunito-regular',
    fontSize: 17,
    color:'red',
    padding:10
  },
  head:
  {
    fontFamily: 'jk-jk',
    fontSize: 25,
    color:'rgb(41, 109, 255)',
    // color:'black', 
    alignSelf:'center',
    // alignItems:'center',
    // justifyContent:'center'
  }
});

export default SomeComponent;
