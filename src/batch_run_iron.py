#!/usr/bin/python

##################################
# Automatically update repository
#
# TODO
# 1. Use cd instead of os.chdir
##################################

import os
from os.path import expanduser
from subprocess import call

targets = [
    "aclservice/server/src/test/scala/com/twitter/aclservice:aclservice",
    "ci/cic/src/test/scala/com/twitter/ci/cic/server:server",
    "ci/cim/src/test/scala:scala",
    "ci/patch/src/test/scala/com/twitter/ci/patch/server:server",
    "ci/service_common/src/test/scala/com/twitter/ci/service_common:service_common",
    "macaw-swift/web-app/src/test/scala/com/twitter/web/config:config",
    "science/tests/java/com/twitter/ads/prediction_service:integration",
    "science/tests/java/com/twitter/adserver/integration:GeoTargetingEndToEndTestIT",
    "trends/trending_content/src/test/scala/com/twitter/trends/trending_content:trending_content",
    "commerce/commerce-core/src/test/scala/com/twitter:twitter",
    "dataproducts/consumption/ctreceiver/src/test/scala/com/twitter/dataproducts/consumption/ctreceiver:ctreceiver",
    "dataproducts/enrichments/delayedenricherator/server/src/test/scala:scala",
    "dataproducts/enrichments/enricherator/server/src/test/scala/com/twitter/dataproducts/enricherator:enricherator",
    "dataproducts/enrichments/locaterator/src/test/scala/com/twitter/locaterator/app:app",
    "dataproducts/eventbusloadtest/src/test/scala/com/twitter/dataproducts/eventbusloadtest:eventbusloadtest",
    "dataproducts/foundation/connection/connection-api/src/test/scala/com/twitter/dataproducts/foundation/connection:connection",
    "discover/macaw-discover/src/test/scala/com/twitter/discover/api/integration:integration",
    "insights/staging-utils/src/test/scala/com/twitter/insights/stagingutils:stagingutils",
    "macaw-digits-api/src/test/scala/com/twitter/macawdigitsapi/integration:integration",
    "manhattan-metaservice/src/test/scala:scala",
    "notificationservice/api/src/test/scala/com/twitter/notificationservice/api:api",
    "pandabear/src/test/scala:scala",
    "science/tests/java/com/twitter/ads/dataservice/associations:unit",
    "science/tests/java/com/twitter/ads/internal/features/impression:impression",
    "science/tests/java/com/twitter/common_internal/text:text",
    "science/tests/java/com/twitter/graph:graph",
    "science/tests/java/com/twitter/search/blender/app/search:search",
    "science/tests/java/com/twitter/search/blender/app/typeahead:typeahead",
    "science/tests/java/com/twitter/search/blender/core/runtime:runtime",
    "science/tests/java/com/twitter/search/blender/core/util:util",
    "science/tests/java/com/twitter/search/blender/services:services",
    "science/tests/java/com/twitter/vit/blender:blender",
    "science/tests/scala/com/twitter/ads/batch/job/apprecord:apprecord",
    "science/tests/scala/com/twitter/ads/batch/job/targeting/topics/evaluation:evaluation",
    "science/tests/scala/com/twitter/statebird/server/v2:v2",
    "science/tests/scala/com/twitter/tip/client:client",
    "spam/rtf/test/scala/com/twitter/spam/rtf/safety_pin:safety_pin",
    "syndication/publisher-97/src/test/scala:scala",
    "timelines/src/test/scala/com/twitter/timelines/external:external",
    "zipbird/intake-service/src/test/scala/com/twitter/zipbird/intake/integration:scala",
]

targets_string = ' '.join(targets)

print "Running {} on IRON with {} parallel jobs ...".format(targets_string, len(targets))
os.chdir(expanduser("~/workspace/source"))
call(["/Users/tzhou/workspace/source/devprod/iron/scripts/user/iron-tryout.sh", targets_string, str(len(targets))])
