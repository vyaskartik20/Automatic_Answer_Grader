
 
import React, {Component} from 'react';
import GestureRecognizer, {swipeDirections} from 'react-native-swipe-gestures';
import { StyleSheet, Text, View, Image, ImageBackground, Button } from 'react-native';
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
    this.props.navigation.push('Instructions')
  }
 
  onSwipeRight(gestureState) {
    this.setState({myText: 'You swiped right!'});
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

    const image1 = { uri: "https://i2.wp.com/www.greaterkashmir.com/wp-content/uploads/2018/02/2018_2largeimg220_feb_2018_002638447.jpg?resize=480%2C320&ssl=1" };
 
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
      
        <View style={styles.container}>
          <ImageBackground source={require('../assets/back3.jpg')} style={styles.background} >
            
            <View style= {styles.last1}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>
            
            <View style={styles.button}>
              <Button 
              title="Download sample OMR " color="grey" 
              onPress={(state)=> this.pressHandler1(state)}
            />
            </View>
            
            <View style= {styles.last2}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>

            <View style={styles.button} color="grey">
              <Button 
                title="Check Marks" 
                onPress={(state)=> this.pressHandler2(state)}
                color="grey" 
              />
            </View> 

            <View style= {styles.last3}>
              {/* <Text style={styles.italics} ></Text> */}
            </View>

            <View style= {styles.last}>
              {/* <FontAwesome name="long-arrow-left" size={30} color="teal" /> */}
              <FontAwesome name="chevron-left" size={20} color="teal" />
              <FontAwesome name="chevron-left" size={20} color="teal" />
              <FontAwesome name="chevron-left" size={20} color="teal" />
              <Text style={styles.italics} > Swipe left for Instructions</Text>
            </View>
          </ImageBackground>
        </View>  



      
      
      
      </GestureRecognizer>
    );
  }
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
    width: 300,
    justifyContent: "center",
    padding: 50,
    flex:1,
    // height:'40%'

  },
  background: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center",
    width: '100%'
  },
  last1: {
    flex:4
  },
  last2: {
    flex:1
  },
  last3: {
    flex:5
  },
  italics:
  {
    fontFamily: 'nunito-regular',
    fontSize: 20,
    color:'teal',
  },
  last : {
    alignItems:'flex-end',
    justifyContent: 'flex-end',
    padding:10,
    flexDirection:'row'
  }
});

export default SomeComponent;