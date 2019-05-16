import { SET_TOKEN, LOGIN } from "../constants/action-types";

const initialState = {
  login: {token: ""}
}

function rootReducer(state = initialState, action) {
  if (action.type === LOGIN) {
    return Object.assign(
      {},
      state,
      Object.assign({}, state.login, {token: action.payload})
    )
  }
  return state;
}

export default rootReducer;
