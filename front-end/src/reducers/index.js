import { combineReducers } from 'redux'

import * as types from '../constants/action_types'

function login(
  state = {
    isLoggedIn: false,
    token: ""
  },
  action
) {
  switch(action.type) {
    case types.LOGIN:
      return Object.assign(
        {},
        state,
        {
          isLoggedIn: true,
          token: action.payload.token
        }
      );
    default:
      return state;
  }
}

function height(state = {}, action) {
  switch(action.type) {
    case types.FREE_HEIGHT:
      return {
        ...state,
        ...action.payload
      };
    default:
      return state;
  }
}

const images = (state = {count: 5}, action) => {
  switch(action.type){
    case types.COUNT:
      return Object.assign({}, state, {...action.count});
    default:
      return state;
  }
}
const rootReducer = combineReducers({
  login,
  images,
  height
});
export default rootReducer;
