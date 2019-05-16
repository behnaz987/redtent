// constants import
import { LOGIN } from "../constants/action-types";

// our new action creator. Will it work?
export function getData() {
  return function(dispatch) {
    return fetch("https://jsonplaceholder.typicode.com/posts")
      .then(response => response.json())
      .then(json => {
        dispatch({ type: "DATA_LOADED", payload: json });
      });
  };
}

// action logic
export function login(payload) {
  return {
    type: LOGIN,
    payload
  };
}
