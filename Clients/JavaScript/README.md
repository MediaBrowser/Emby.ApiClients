# EmbyClient.JavaScript

EmbyClientJavaScript - JavaScript client for EmbyClient.JavaScript
Explore the Emby Server API

- API version: 4.8.0.3
- Package version: 0.0.0.0
- Build package: io.swagger.codegen.v3.generators.javascript.JavaScriptClientCodegen
For more information, please visit [https://emby.media/community/index.php?/forum/47-developer-api](https://emby.media/community/index.php?/forum/47-developer-api)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install EmbyClient.JavaScript --save
```

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var EmbyClientJavaScript = require('EmbyClient.JavaScript');
var defaultClient = EmbyClientJavaScript.ApiClient.instance;

// Configure API key authorization: apikeyauth
var apikeyauth = defaultClient.authentications['apikeyauth'];
apikeyauth.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikeyauth.apiKeyPrefix['api_key'] = "Token"


var api = new EmbyClientJavaScript.ActivityLogServiceApi()
var opts = { 
  'startIndex': 56, // {Number} Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // {Number} Optional. The maximum number of records to return
  'minDate': "minDate_example" // {String} Optional. The minimum date. Format = ISO
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getSystemActivitylogEntries(opts, callback);
```

