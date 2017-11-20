// TODO(DEVELOPER): Change the values below using values from the initialization snippet: Firebase Console > Overview > Add Firebase to your web app.
// Initialize Firebase
var config = {
  apiKey: "AIzaSyCZCs7PIno3eKWR1u-CR5Ua9AqPLPFwluw",
  authDomain: "tolc-b0fa5.firebaseapp.com",
  databaseURL: "https://tolc-b0fa5.firebaseio.com",
  projectId: "tolc-b0fa5",
  storageBucket: "tolc-b0fa5.appspot.com",
  messagingSenderId: "62715960283"
};
firebase.initializeApp(config);


 var bookmark_div = document.getElementById("bookmark");

 var name;
 var url;
 var tags;


/**
 * initApp handles setting up the Firebase context and registering
 * callbacks for the auth status.
 *
 * The core initialization is in firebase.App - this is the glue class
 * which stores configuration. We provide an app name here to allow
 * distinguishing multiple app instances.
 *
 * This method also registers a listener with firebase.auth().onAuthStateChanged.
 * This listener is called when the user is signed in or out, and that
 * is where we update the UI.
 *
 * When signed in, we also authenticate to the Firebase Realtime Database.
 */
function initApp() {
  // Listen for auth state changes.
  // [START authstatelistener]
  firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      // User is signed in.
      console.log("works-inside credentials.js");

      var displayName = user.displayName;
      var email = user.email;
      var emailVerified = user.emailVerified;
      var photoURL = user.photoURL;
      var isAnonymous = user.isAnonymous;
      var uid = user.uid;
      var refreshToken = user.refreshToken;
      var providerData = user.providerData;
      // [START_EXCLUDE]
      document.getElementById('quickstart-button').textContent = 'Sign out';
      document.getElementById('quickstart-sign-in-status').textContent = 'Signed in';

      document.getElementById('quickstart-account-details').textContent = JSON.stringify({
        displayName: displayName,
        email: email,
        emailVerified: emailVerified,
        photoURL: photoURL,
        isAnonymous: isAnonymous,
        uid: uid,
        refreshToken: refreshToken,
        providerData: providerData
      }, null, '  ');
      // [END_EXCLUDE]

    } else {
      // Let's try to get a Google auth token programmatically.
      // [START_EXCLUDE]
      document.getElementById('quickstart-button').textContent = 'Sign-in with Google';
      document.getElementById('quickstart-sign-in-status').textContent = 'Signed out';
      document.getElementById('quickstart-account-details').textContent = 'null';
      // [END_EXCLUDE]
    }
    document.getElementById('quickstart-button').disabled = false;
  });
  // [END authstatelistener]

  document.getElementById('quickstart-button').addEventListener('click', startSignIn, false);

}

/**
 * Start the auth flow and authorizes to Firebase.
 * @param{boolean} interactive True if the OAuth flow should request with an interactive mode.
 */
function startAuth(interactive) {
  // Request an OAuth token from the Chrome Identity API.
  chrome.identity.getAuthToken({interactive: !!interactive}, function(token) {
    if (chrome.runtime.lastError && !interactive) {
      console.log('It was not possible to get a token programmatically.');
    } else if(chrome.runtime.lastError) {
      console.error(chrome.runtime.lastError);
    } else if (token) {
      // Authrorize Firebase with the OAuth Access Token.
      var credential = firebase.auth.GoogleAuthProvider.credential(null, token);
      firebase.auth().signInWithCredential(credential).catch(function(error) {
        // The OAuth token might have been invalidated. Lets' remove it from cache.
        if (error.code === 'auth/invalid-credential') {
          chrome.identity.removeCachedAuthToken({token: token}, function() {
            startAuth(interactive);
          });
        }
      });
    } else {
      console.error('The OAuth Token was null');
    }
  });
}

/**
 * Starts the sign-in process.
 */
function startSignIn() {
  document.getElementById('quickstart-button').disabled = true;
  if (firebase.auth().currentUser) {
    firebase.auth().signOut();
  } else {
    startAuth(true);
  }
}


function startSubscribe()
{
  document.getElementById('subscribe-button').textContent = 'Sign-in with Google';

  firebase.messaging().requestPermission()
.then(function() {
  setStatus("Notification permission granted.");
  // TODO(developer): Retrieve an Instance ID token for use with FCM.
  // ...
  firebase.messaging().getToken().then((token) => {
    console.log(token)
    console.log(firebase.auth().currentUser.displayName)
  });
})
.catch(function(err) {
  setStatus('Unable to get permission to notify.', err);
});
firebase.database().ref('/references').once('value', function(snapshot) {
 document.getElementById("status").innerHTML = "ref";
 console.log(snapshot.val());
   // document.getElementById("status").innerHTML=snapshot;
});

//chrome.instanceID.getID(getId)

}


function addBookmark(e)
{
  e.preventDefault();
  const url = document.getElementById('url').value;
  const title = document.getElementById('title').value;
  const note = document.getElementById('notes').value;
  firebase.database().ref('/references')
    .push({
      user: firebase.auth().currentUser.displayName,
      url: url,
      title: title,
      note: note,
      userProfileImg: firebase.auth().currentUser.photoURL,
      date: Date()
    })
    .then(() => {
      console.log("reference has been added");
      document.getElementById('url').value = "";
      document.getElementById('title').value = "";
      document.getElementById('notes').value = "";
    })
    .catch(() => {
      console.log("error adding reference :(")
    });
}

function getId(senderId)
{
  chrome.gcm.register([senderId], registerCallback);
  setStatus("Registering ...");
}

function registerCallback(regId) {
  registrationId = regId;
  if (chrome.runtime.lastError) {
    // When the registration fails, handle the error and retry the
    // registration later.
    setStatus("Registration failed: " + chrome.runtime.lastError.message);
    return;
  }
  firebase.database().ref('/tokens').push({
      token: registrationId,
      username: firebase.auth().currentUser.displayName,
      uid: firebase.auth().currentUser.uid
    });

  // Mark that the first-time registration is done.
  setStatus("Registration succeeded.");
  chrome.storage.local.set({registered: true});
  firebase.database().ref('/data').push({
      data: "work",
      username: firebase.auth().currentUser.displayName,
      date: Date()
    });


firebase.database().ref('/data').once('value', function(snapshot) {
 document.getElementById("status").innerHTML = "success1";
 console.log(snapshot.val());
   // document.getElementById("status").innerHTML=snapshot;
});

chrome.gcm.onMessage.addListener(function(message) {
  document.getElementById("status").innerHTML = "success";
 // document.getElementById("status").innerHTML=message.key() + " " + message.val();
});
}

$('#closePopUp').click(function(event) {
window.close();
});

function setStatus(status) {
  document.getElementById("status").innerHTML = status;
}

function getURL() {

  chrome.runtime.getBackgroundPage(function(eventPage) {
          // Call the getPageInfo function in the background page, passing in
          // our onPageDetailsReceived function as the callback. This injects
          // content.js into the current tab's HTML
          eventPage.getPageDetails(onPageDetailsReceived);
      });
}

function onPageDetailsReceived(pageDetails)  {
    // document.getElementById('title').value = pageDetails.title;
    // document.getElementById('url').value = pageDetails.url;
    // document.getElementById('summary').innerText = pageDetails.summary;
    console.log(pageDetails.url)
    url = pageDetails.url;
    document.getElementById('url').value = pageDetails.url;
}

window.onload = function() {
    document.getElementById('subscribe-button').addEventListener('click', startSubscribe);
    document.getElementById('addbookmark-button').addEventListener('click', addBookmark);
    document.getElementById('chatbotbtn').addEventListener('click', changePage);
    getURL();
  initApp();
};

function changePage(){
  console.log("Button clicked")
  window.location.href="chatbot.html";
}
