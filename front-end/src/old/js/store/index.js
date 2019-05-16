// import modules
import { createStore } from "redux";

// import src
import rootReducer from "../reducers/index";

// store logic
const store = createStore(
  rootReducer,
);

export default store;
