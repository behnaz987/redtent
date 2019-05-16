import axios from 'axios';

import * as types from '../constants/action_types';
import API from '../components/API';

const login = (payload) => { 
  return {
    type: types.LOGIN,
    payload
  }; 
};

export function postUserData(userData, postType) {
  return async function(dispatch) {

    let postAPI;
    if (postType === "SIGNUP") postAPI = API.signUp;
    else if(postType === "SIGNIN") postAPI = API.signIn;
    else postAPI = API.signIn;

    return axios.post(postAPI, userData)
                .then((response) => dispatch(login(response.data)))
                .catch((error) => console.log(error));
  }
}

// const images = (payload) => {
//   return {
//     type: types.IMAGES,
//     payload
//   }
// }

// export function fetchImages(from, row) {
//   return async function(dispatch) {
//     // let mostViewd = [];
//     // let top = [];  

//     // axios.get(
//     //   `${API.items}_from=${from}&_row=${row}&_order_by=view`
//     // ).then((response) => dispatch(images(response.data)))
//     //   .catch((error) => console.log(error));
       
//     // axios.get(
//     //   `${API.items}_from=${from}&_row=${row}&_order_by=total_rate`
//     // ).then((response) => top = response.data)
//     //   .catch((error) => console.log(error));
    
//     // const imagesCollection = [...new Set([...mostViewd, ...top])];

//     // return dispatch(images(imagesCollection));
//   }
// }

export const freeHeight = (payload) => {
  return {
    type: types.FREE_HEIGHT,
    payload
  }
}

export function getFreeHeight(payload) {
  return async function(dispatch){
    return dispatch(freeHeight(payload));
  }
}
