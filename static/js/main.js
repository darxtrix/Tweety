// navigate between the tweets
function navigate(tweets,tweetBox) {
    var currValue = 0;
    var previous = document.getElementById('previousTweet');
    var next = document.getElementById('nextTweet');
    previous.addEventListener('click',function(){
        currValue = ( currValue-1 >= 0 ) ? ( --currValue) : (tweets.length-1);
        tweetBox.innerHTML = tweets[currValue];
    },false);
    next.addEventListener('click',function(){
        currValue = ( currValue + 1 < (tweets.length-1) ) ? ( ++currValue) : 0;
        tweetBox.innerHTML = tweets[currValue];
    },false);
}

// send ajax request to the server
// :param: tweetBox Where the tweets are to be shown to the user
// :param: userInput twitter handle input box
function fetchTweets(tweetBox,userInput,submitBtn) {
    var request = new XMLHttpRequest();
    var screen_name = userInput.value;
    var requestUrl = '/get_tweets/?screen_name=' + screen_name;
    console.log(requestUrl);
    request.open("GET",requestUrl,true);
    request.send();
    submitBtn.innerHTML = '<i class="fa fa-spinner"></i>';
    var response;
    request.onreadystatechange = function() {
        if (request.readyState === 4 && request.status === 200) {
            submitBtn.innerHTML = 'Generate';
            response = JSON.parse(request.response);
            if ( 'errors' in response ) {
                document.querySelector('#error').innerHTML = response.errors;
            }
            else {
                document.querySelector('#error').innerHTML = '';
                tweetBox.innerHTML = response.tweets[0];
                userInput.value = response.screen_name;
                document.querySelector('#tweetWrapper').style.display = 'block';
                navigate(response.tweets,tweetBox);
            }
        }
    }
}

// send a request when the user clicks on the form submit button
(function() {
    console.log('I m happening');
    var submitBtn = document.getElementById('fetchTweets');
    var tweetBox = document.getElementById('tweetBox');
    var userInput = document.getElementById('handle');
    submitBtn.addEventListener('click',function(e) {
        fetchTweets(tweetBox,userInput,submitBtn);
    },false);
})();