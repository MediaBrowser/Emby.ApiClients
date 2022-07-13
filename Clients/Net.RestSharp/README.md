# EmbyClient.Dotnet - the C# library for the Emby Server REST API (BETA)

Explore the Emby Server API

- API version: 4.8.0.3
- SDK version: 0.0.0.0
    For more information, please visit [https://emby.media/community/index.php?/forum/47-developer-api](https://emby.media/community/index.php?/forum/47-developer-api)

<a name="frameworks-supported"></a>
## Frameworks supported
- .NET Core >=2.0
- .NetStandard 2.0
- .NET Framework >=4.6
- Mono/Xamarin >=vNext
- UWP >=10.0

<a name="dependencies"></a>
## Dependencies
- [RestSharp](https://www.nuget.org/packages/RestSharp) - 106.2.2 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 10.0.3 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the packages:
```
Install-Package RestSharp
Install-Package Newtonsoft.Json
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742)

<a name="installation"></a>
## Installation
Run the following command to generate the DLL
- [Mac/Linux] `/bin/sh build.sh`
- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:
```csharp
using EmbyClient.Dotnet.Api;
using EmbyClient.Dotnet.Client;
using EmbyClient.Dotnet.Model;
```
<a name="packaging"></a>
## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package) and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package) packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj` directly:

```
nuget pack -Build -OutputDirectory out EmbyClient.Dotnet.csproj
```

Then, publish to a [local feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and consume the new package via Nuget as usual.

<a name="getting-started"></a>
## Getting Started

```csharp
using System;
using System.Diagnostics;
using EmbyClient.Dotnet.Api;
using EmbyClient.Dotnet.Client;
using EmbyClient.Dotnet.Model;

namespace Example
{
    public class Example
    {
        public void main()
        {
            // Configure API key authorization: apikeyauth
            Configuration.Default.ApiKey.Add("api_key", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.ApiKeyPrefix.Add("api_key", "Bearer");

            var apiInstance = new ActivityLogServiceApi();
            var startIndex = 56;  // int? | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional) 
            var limit = 56;  // int? | Optional. The maximum number of records to return (optional) 
            var minDate = minDate_example;  // string | Optional. The minimum date. Format = ISO (optional) 

            try
            {
                // Gets activity log entries
                QueryResultActivityLogEntry result = apiInstance.GetSystemActivitylogEntries(startIndex, limit, minDate);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ActivityLogServiceApi.GetSystemActivitylogEntries: " + e.Message );
            }
        }
    }
}
```

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://emby.media/emby*

