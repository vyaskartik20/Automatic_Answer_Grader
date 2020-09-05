import React from 'react';
import { StyleSheet, Text, View, Image, ImageBackground, Button, TouchableOpacity, Linking} from 'react-native';

export default function Download( {navigation} )  {
    
  return (
    <View style={styles.container}>
          <ImageBackground source={require('../assets/back3.jpg')} style={styles.background} >

            <View style={styles.button}>
              <Button 
                title="10 QUESTIONS " 
                color="grey" 
                onPress={ ()=> Linking.openURL('https://drive.google.com/file/d/1cVUdUM2Lb_XQ8WGkcfLzM4JBHLtePeX4/view')}
              />
            </View>

            <View style={styles.button} color="grey">
              <Button 
                title="20 QUESTIONS" 
                color="grey" 
                onPress={ ()=> Linking.openURL('https://drive.google.com/file/d/1IW7QEdphEOZcSXwfgcJhlBp0OjxP3UjY/view')}
              />
            </View> 

            <View style={styles.button}>
              <Button 
                title="30 QUESTIONS" 
                color="grey" 
                onPress={ ()=> Linking.openURL('https://drive.google.com/file/d/19jTJa39Um0KgDMlxkUhSjgPRKroXDkGA/view')}
              />
            </View>

            <View style={styles.button} color="grey">
              <Button 
                title="40 QUESTIONS" 
                color="grey" 
                onPress={ ()=> Linking.openURL('https://drive.google.com/file/d/1lyMJMhbxz2LcBBbBy92Poayo1aPZX98Q/view')}
              />
            </View> 

            <View style={styles.button} color="grey">
              <Button 
                title="60 QUESTIONS" 
                color="grey" 
                onPress={ ()=> Linking.openURL('https://drive.google.com/file/d/1SGa2oOj6MeVnSddquJ6sle278xofTSeY/view')}
              />
            </View> 
{/* 
            <View style={styles.button} color="grey">
              <TouchableOpacity>
                <Text>80 Questions</Text>
              </TouchableOpacity>
            </View>  */}





          </ImageBackground>
      </View>  
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'teal',
    alignItems: 'center',
    justifyContent: 'center',
  },
  colour: {
    // flex: 1,
    fontSize : 28,
    justifyContent: "center",
    // color: 'white'
  },

  button: {
    color: 'red',
    width: 300,
    justifyContent: "center",
    padding: 10,
    margin: 30
  },
  background: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center",
    alignItems: 'center',
    width: '100%'
  }
});