import{ createStackNavigator } from 'react-navigation-stack';
import {createAppContainer} from 'react-navigation';
// import { fromLeft, fromRight, fromBottom } from 'react-navigation-transitions'
import Home from '../screens/home';
import Capture3 from '../screens/capture3';
import Capture1 from '../screens/capture1';
import Capture2 from '../screens/capture2';
import First from '../screens/first';
import Intro from '../screens/intro';
import Third from '../screens/third';
import Download from '../screens/download';
import HomeScreen from '../screens/home';
import SomeComponent from '../screens/home';
import Instructions from '../screens/instructions';
import Picker3 from '../screens/picker3';
import Picker2 from '../screens/picker2';
import Picker1 from '../screens/picker1';


const screens = {

    Intro: {
        screen :Intro,
        navigationOptions: {
            headerShown: false
        }
    },
    Picker3: {
        screen :Picker3,
        navigationOptions: {
            headerShown: false
        }
    },
    Picker2: {
        screen :Picker2,
        navigationOptions: {
            headerShown: false
        }
    },
    Picker1: {
        screen :Picker1,
        navigationOptions: {
            headerShown: false
        }
    },
    SomeComponent: {
        screen :SomeComponent,
        navigationOptions: {
            headerShown: false
        }
    },
    Instructions: {
        screen :Instructions,
        navigationOptions: {
            headerShown: false
        }
    },
    Home: {
        screen: Home,
        navigationOptions: {
            headerShown: false
        }
    },
    HomeScreen: {
        screen: HomeScreen,
        navigationOptions: {
            headerShown: false
        }
    },
    Capture1: {
        screen:Capture1,
        navigationOptions: {
            headerShown: false
        }
    },
    Capture2: {
        screen:Capture2,
        navigationOptions: {
            headerShown: false
        }
    },
    Capture3: {
        screen:Capture3,
        navigationOptions: {
            headerShown: false
        }
    },
    First: {
        screen: First,
        navigationOptions: {
            headerShown: false
        }
    },
    Third: {
        screen: Third,
        navigationOptions: {
            headerShown: false
        }
    },
    Download: {
        screen: Download,
        navigationOptions: {
            headerShown: false
        }
    }

}

const HomeStack= createStackNavigator(screens);

export default createAppContainer(HomeStack);