// import React, { Component } from 'react';
// import {
//   View,
//   Dimensions,
//   Button,
//   Share,
// } from 'react-native';
// import { Constants} from 'expo';
// import * as FileSystem from 'expo-file-system';

// export default class App extends Component {
//   static navigationOptions = {
//     title: 'Pdf Screen',
//   };

//   state = {
//     pdfUrl: '',
//   };

//    makeDowload() {
//        FileSystem.downloadAsync(
//       'http://gahp.net/wp-content/uploads/2017/09/sample.pdf',
//       FileSystem.documentDirectory + 'small.pdf'
//     )
//       .then(({ uri }) => {
//         console.log('Finished downloading to ', uri);
//         alert(FileSystem.documentDirectory);
//       })
//       .catch(error => {
//         console.error(error);
//       });

//   }

//   render() {
//     return (
//       <View
//         style={{
//           flex: 1,
//           alignItems: 'center',
//           justifyContent: 'center',
//           margin: 10,
//         }}
//       >
//         <Button          
//           title="baixar"
//           onPress={() => {
//             this.makeDowload();
//           }}/>
//       </View>
//     );
//   }
// }



// import React from 'react';
// import { StyleSheet, Dimensions, View } from 'react-native';
 
// import Pdf from 'react-native-pdf';
 
// export default class PDFExample extends React.Component {
//     render() {
//         const source = {uri:'http://samples.leanpub.com/thereactnativebook-sample.pdf',cache:true};
//         //const source = require('./test.pdf');  // ios only
//         //const source = {uri:'bundle-assets://test.pdf'};
 
//         //const source = {uri:'file:///sdcard/test.pdf'};
//         //const source = {uri:"data:application/pdf;base64,JVBERi0xLjcKJc..."};
 
//         return (
//             <View style={styles.container}>
//                 <Pdf
//                     source={source}
//                     onLoadComplete={(numberOfPages,filePath)=>{
//                         console.log(`number of pages: ${numberOfPages}`);
//                     }}
//                     onPageChanged={(page,numberOfPages)=>{
//                         console.log(`current page: ${page}`);
//                     }}
//                     onError={(error)=>{
//                         console.log(error);
//                     }}
//                     onPressLink={(uri)=>{
//                         console.log(`Link presse: ${uri}`)
//                     }}
//                     style={styles.pdf}/>
//             </View>
//         )
//   }
// }
 
// const styles = StyleSheet.create({
//     container: {
//         flex: 1,
//         justifyContent: 'flex-start',
//         alignItems: 'center',
//         marginTop: 25,
//     },
//     pdf: {
//         flex:1,
//         width:Dimensions.get('window').width,
//         height:Dimensions.get('window').height,
//     }
// });




import React, { useState } from 'react';
import Intro from './screens/intro';
import * as Font from 'expo-font';
import { AppLoading } from 'expo';
import Navigator from './routes/homeStack';

const getFonts = () => Font.loadAsync({
  'nunito-regular': require('./assets/fonts/BalsamiqSans-Italic.ttf'),
  'jk-jk': require('./assets/fonts/Nunito-Regular.ttf'),
  'nunito-bold': require('./assets/fonts/Nunito-ExtraLightItalic.ttf'),
  'italy-1':require('./assets/fonts/ArchitectsDaughter-Regular.ttf'),
});

export default function App() {
  const [fontsLoaded, setFontsLoaded] = useState(false);

  if (fontsLoaded) {
    return (
      <Navigator />
    );
  } else {
    return (
      <AppLoading 
        startAsync={getFonts} 
        onFinish={() => setFontsLoaded(true)} 
      />
    )
  }
}