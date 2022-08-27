import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

clients = {
  "op" : {
    "name" : "op",
    "environment" : ['acc', 'demo', 'prod']
  }
}
for client in clients.values():
    for env in client["environment"]:
        #print(env)
        url1 = 'https://jenkins/job/customers/job/%s/job/%s-%s-backup-dbs/api/json' % (client["name"], client["name"], env)
        # Your jenkins URL and credentials goes here
        #url = 'https://jenkins.treasurup.com/job/customers/job/rabo-rn/job/rabo-rn-acc-backup-dbs/api/json'
        username = 'admin'
        password = ''

        # Use the 'auth' parameter to send requests with HTTP Basic Auth:
        # Accessing the Job page to get the latest Build ran.
        response = requests.post(url1, auth=(username, password), verify=False)

        try:
            buildnumberJson = json.loads(response.text)
            print(buildnumberJson['lastBuild']['number'])
            print(buildnumberJson['lastUnsuccessfulBuild']['number'])
            #print(buildnumberJson['lastFailedBuild'])

            if buildnumberJson['lastBuild']['number'] == buildnumberJson['lastUnsuccessfulBuild']['number']:
                print('Last build is an unsuccesssful Build/ Failed build')
            else:
                print('Last build is not an unsuccessfull build / Failed build')
        except:
            print("Failed to parse json")

        if "lastBuild" in buildnumberJson:
            totalbuilds = buildnumberJson["lastBuild"]
            runs = totalbuilds["number"]

        else:
            print("Failed to get build")










# # Iterate over the job build runs to get the build status for each
#
# totalsuccess = totalfailure = totalmissing = 0
#
# for build in range(1, runs):
#     buildurl = 'https://jenkins.treasurup.com/job/customers/job/rabo-rn/job/rabo-rn-acc-backup-dbs/' + str(build) + '/api/json'
#     print(buildurl)
#     buildstatus = []
#     try:
#         response = requests.post(buildurl, auth=(username, password), verify=False)
#         buildstatus = json.loads(response.text)
#     except Exception as e:
#         totalmissing = totalmissing + 1
#     if "result" in buildstatus:
#         if buildstatus["result"] == "SUCCESS":
#             totalsuccess = totalsuccess + 1
#         if buildstatus["result"] == "FAILURE":
#             totalfailure = totalfailure + 1
#
# # Generate Output numbers
#
# print(f"total builds:{runs}")
# print(f"total succeeded builds:{totalsuccess}")
# print(f"total failed builds:{totalfailure}")
# print(f"total skipped builds:{totalmissing}")