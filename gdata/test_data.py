#!/usr/bin/python
#
# Copyright (C) 2006 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



XML_ENTRY_1 = """<?xml version='1.0'?>
<entry xmlns='http://www.w3.org/2005/Atom'
       xmlns:g='http://base.google.com/ns/1.0'>
  <category scheme="http://base.google.com/categories/itemtypes"
            term="products"/>
  <id>    http://www.google.com/test/id/url   </id>
  <title type='text'>Testing 2000 series laptop</title>
  <content type='xhtml'>
    <div xmlns='http://www.w3.org/1999/xhtml'>A Testing Laptop</div>
  </content>
  <link rel='alternate' type='text/html'
        href='http://www.provider-host.com/123456789'/>
  <link rel='license' 
        href='http://creativecommons.org/licenses/by-nc/2.5/rdf'/>
  <g:label>Computer</g:label>
  <g:label>Laptop</g:label>
  <g:label>testing laptop</g:label>
  <g:item_type>products</g:item_type>
</entry>"""


TEST_BASE_ENTRY = """<?xml version='1.0'?>
<entry xmlns='http://www.w3.org/2005/Atom'
       xmlns:g='http://base.google.com/ns/1.0'>
  <category scheme="http://base.google.com/categories/itemtypes"
            term="products"/>
  <title type='text'>Testing 2000 series laptop</title>
  <content type='xhtml'>
    <div xmlns='http://www.w3.org/1999/xhtml'>A Testing Laptop</div>
  </content>
  <app:control xmlns:app='http://purl.org/atom/app#'>
    <app:draft>yes</app:draft>
    <gm:disapproved xmlns:gm='http://base.google.com/ns-metadata/1.0'/>   
  </app:control>
  <link rel='alternate' type='text/html'
        href='http://www.provider-host.com/123456789'/>
  <g:label>Computer</g:label>
  <g:label>Laptop</g:label>
  <g:label>testing laptop</g:label>
  <g:item_type>products</g:item_type>
</entry>"""


BIG_FEED = """<?xml version="1.0" encoding="utf-8"?>
   <feed xmlns="http://www.w3.org/2005/Atom">
     <title type="text">dive into mark</title>
     <subtitle type="html">
       A &lt;em&gt;lot&lt;/em&gt; of effort
       went into making this effortless
     </subtitle>
     <updated>2005-07-31T12:29:29Z</updated>
     <id>tag:example.org,2003:3</id>
     <link rel="alternate" type="text/html"
      hreflang="en" href="http://example.org/"/>
     <link rel="self" type="application/atom+xml"
      href="http://example.org/feed.atom"/>
     <rights>Copyright (c) 2003, Mark Pilgrim</rights>
     <generator uri="http://www.example.com/" version="1.0">
       Example Toolkit
     </generator>
     <entry>
       <title>Atom draft-07 snapshot</title>
       <link rel="alternate" type="text/html"
        href="http://example.org/2005/04/02/atom"/>
       <link rel="enclosure" type="audio/mpeg" length="1337"
        href="http://example.org/audio/ph34r_my_podcast.mp3"/>
       <id>tag:example.org,2003:3.2397</id>
       <updated>2005-07-31T12:29:29Z</updated>
       <published>2003-12-13T08:29:29-04:00</published>
       <author>
         <name>Mark Pilgrim</name>
         <uri>http://example.org/</uri>
         <email>f8dy@example.com</email>
       </author>
       <contributor>
         <name>Sam Ruby</name>
       </contributor>
       <contributor>
         <name>Joe Gregorio</name>
       </contributor>
       <content type="xhtml" xml:lang="en"
        xml:base="http://diveintomark.org/">
         <div xmlns="http://www.w3.org/1999/xhtml">
           <p><i>[Update: The Atom draft is finished.]</i></p>
         </div>
       </content>
     </entry>
   </feed>
"""

SMALL_FEED = """<?xml version="1.0" encoding="utf-8"?>
   <feed xmlns="http://www.w3.org/2005/Atom">
     <title>Example Feed</title>
     <link href="http://example.org/"/>
     <updated>2003-12-13T18:30:02Z</updated>
     <author>
       <name>John Doe</name>
     </author>
     <id>urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6</id>
     <entry>
       <title>Atom-Powered Robots Run Amok</title>
       <link href="http://example.org/2003/12/13/atom03"/>
       <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
       <updated>2003-12-13T18:30:02Z</updated>
       <summary>Some text.</summary>
     </entry>
   </feed>
"""

GBASE_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:g='http://base.google.com/ns/1.0' xmlns:batch='http://schemas.google.com/gdata/batch'>
<id>http://www.google.com/base/feeds/snippets</id>
<updated>2007-02-08T23:18:21.935Z</updated>
<title type='text'>Items matching query: digital camera</title>
<link rel='alternate' type='text/html' href='http://base.google.com'>
</link>
<link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets'>
</link>
<link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets?start-index=1&amp;max-results=25&amp;bq=digital+camera'>
</link>
<link rel='next' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets?start-index=26&amp;max-results=25&amp;bq=digital+camera'>
</link>
<generator version='1.0' uri='http://base.google.com'>GoogleBase              </generator>
<openSearch:totalResults>2171885</openSearch:totalResults>
<openSearch:startIndex>1</openSearch:startIndex>
<openSearch:itemsPerPage>25</openSearch:itemsPerPage>
<entry>
<id>http://www.google.com/base/feeds/snippets/13246453826751927533</id>
<published>2007-02-08T13:23:27.000Z</published>
<updated>2007-02-08T16:40:57.000Z</updated>
<category scheme='http://base.google.com/categories/itemtypes' term='Products'>
</category>
<title type='text'>Digital Camera Battery Notebook Computer 12v DC Power Cable - 5.5mm x 2.5mm (Center +) Camera Connecting Cables</title>
<content type='html'>Notebook Computer 12v DC Power Cable - 5.5mm x 2.1mm (Center +) This connection cable will allow any Digital Pursuits battery pack to power portable computers that operate with 12v power and have a 2.1mm power connector (center +) Digital  ...</content>
<link rel='alternate' type='text/html' href='http://www.bhphotovideo.com/bnh/controller/home?O=productlist&amp;A=details&amp;Q=&amp;sku=305668&amp;is=REG&amp;kw=DIDCB5092&amp;BI=583'>
</link>
<link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets/13246453826751927533'>
</link>
<author>
<name>B&amp;H Photo-Video</name>
<email>anon-szot0wdsq0at@base.google.com</email>
</author>
<g:payment_notes type='text'>PayPal &amp; Bill Me Later credit available online only.</g:payment_notes>
<g:condition type='text'>new</g:condition>
<g:location type='location'>420 9th Ave. 10001</g:location>
<g:id type='text'>305668-REG</g:id>
<g:item_type type='text'>Products</g:item_type>
<g:brand type='text'>Digital Camera Battery</g:brand>
<g:expiration_date type='dateTime'>2007-03-10T13:23:27.000Z</g:expiration_date>
<g:customer_id type='int'>1172711</g:customer_id>
<g:price type='floatUnit'>34.95 usd</g:price>
<g:product_type type='text'>Digital Photography&gt;Camera Connecting Cables</g:product_type>
<g:item_language type='text'>EN</g:item_language>
<g:manufacturer_id type='text'>DCB5092</g:manufacturer_id>
<g:target_country type='text'>US</g:target_country>
<g:weight type='float'>1.0</g:weight>
<g:image_link type='url'>http://base.google.com/base_image?q=http%3A%2F%2Fwww.bhphotovideo.com%2Fimages%2Fitems%2F305668.jpg&amp;dhm=ffffffff84c9a95e&amp;size=6</g:image_link>
</entry>
<entry>
<id>http://www.google.com/base/feeds/snippets/10145771037331858608</id>
<published>2007-02-08T13:23:27.000Z</published>
<updated>2007-02-08T16:40:57.000Z</updated>
<category scheme='http://base.google.com/categories/itemtypes' term='Products'>
</category>
<title type='text'>Digital Camera Battery Electronic Device 5v DC Power Cable - 5.5mm x 2.5mm (Center +) Camera Connecting Cables</title>
<content type='html'>Electronic Device 5v DC Power Cable - 5.5mm x 2.5mm (Center +) This connection cable will allow any Digital Pursuits battery pack to power any electronic device that operates with 5v power and has a 2.5mm power connector (center +) Digital  ...</content>
<link rel='alternate' type='text/html' href='http://www.bhphotovideo.com/bnh/controller/home?O=productlist&amp;A=details&amp;Q=&amp;sku=305656&amp;is=REG&amp;kw=DIDCB5108&amp;BI=583'>
</link>
<link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets/10145771037331858608'>
</link>
<author>
<name>B&amp;H Photo-Video</name>
<email>anon-szot0wdsq0at@base.google.com</email>
</author>
<g:location type='location'>420 9th Ave. 10001</g:location>
<g:condition type='text'>new</g:condition>
<g:weight type='float'>0.18</g:weight>
<g:target_country type='text'>US</g:target_country>
<g:product_type type='text'>Digital Photography&gt;Camera Connecting Cables</g:product_type>
<g:payment_notes type='text'>PayPal &amp; Bill Me Later credit available online only.</g:payment_notes>
<g:id type='text'>305656-REG</g:id>
<g:image_link type='url'>http://base.google.com/base_image?q=http%3A%2F%2Fwww.bhphotovideo.com%2Fimages%2Fitems%2F305656.jpg&amp;dhm=7315bdc8&amp;size=6</g:image_link>
<g:manufacturer_id type='text'>DCB5108</g:manufacturer_id>
<g:upc type='text'>838098005108</g:upc>
<g:price type='floatUnit'>34.95 usd</g:price>
<g:item_language type='text'>EN</g:item_language>
<g:brand type='text'>Digital Camera Battery</g:brand>
<g:customer_id type='int'>1172711</g:customer_id>
<g:item_type type='text'>Products</g:item_type>
<g:expiration_date type='dateTime'>2007-03-10T13:23:27.000Z</g:expiration_date>
</entry>
<entry>
<id>http://www.google.com/base/feeds/snippets/3128608193804768644</id>
<published>2007-02-08T02:21:27.000Z</published>
<updated>2007-02-08T15:40:13.000Z</updated>
<category scheme='http://base.google.com/categories/itemtypes' term='Products'>
</category>
<title type='text'>Digital Camera Battery Power Cable for Kodak 645 Pro-Back ProBack &amp; DCS-300 Series Camera Connecting Cables</title>
<content type='html'>Camera Connection Cable - to Power Kodak 645 Pro-Back DCS-300 Series Digital Cameras This connection cable will allow any Digital Pursuits battery pack to power the following digital cameras: Kodak DCS Pro Back 645 DCS-300 series Digital Photography ...</content>
<link rel='alternate' type='text/html' href='http://www.bhphotovideo.com/bnh/controller/home?O=productlist&amp;A=details&amp;Q=&amp;sku=305685&amp;is=REG&amp;kw=DIDCB6006&amp;BI=583'>
</link>
<link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/snippets/3128608193804768644'>
</link>
<author>
<name>B&amp;H Photo-Video</name>
<email>anon-szot0wdsq0at@base.google.com</email>
</author>
<g:weight type='float'>0.3</g:weight>
<g:manufacturer_id type='text'>DCB6006</g:manufacturer_id>
<g:image_link type='url'>http://base.google.com/base_image?q=http%3A%2F%2Fwww.bhphotovideo.com%2Fimages%2Fitems%2F305685.jpg&amp;dhm=72f0ca0a&amp;size=6</g:image_link>
<g:location type='location'>420 9th Ave. 10001</g:location>
<g:payment_notes type='text'>PayPal &amp; Bill Me Later credit available online only.</g:payment_notes>
<g:item_type type='text'>Products</g:item_type>
<g:target_country type='text'>US</g:target_country>
<g:accessory_for type='text'>digital kodak camera</g:accessory_for>
<g:brand type='text'>Digital Camera Battery</g:brand>
<g:expiration_date type='dateTime'>2007-03-10T02:21:27.000Z</g:expiration_date>
<g:item_language type='text'>EN</g:item_language>
<g:condition type='text'>new</g:condition>
<g:price type='floatUnit'>34.95 usd</g:price>
<g:customer_id type='int'>1172711</g:customer_id>
<g:product_type type='text'>Digital Photography&gt;Camera Connecting Cables</g:product_type>
<g:id type='text'>305685-REG</g:id>
</entry>
</feed>"""

EXTENSION_TREE = """<?xml version="1.0" encoding="utf-8"?>
   <feed xmlns="http://www.w3.org/2005/Atom">
     <g:author xmlns:g="http://www.google.com">
       <g:name>John Doe
         <g:foo yes="no" up="down">Bar</g:foo>
       </g:name>
     </g:author>
   </feed>
"""

TEST_AUTHOR = """<?xml version="1.0" encoding="utf-8"?>
   <author xmlns="http://www.w3.org/2005/Atom">
       <name xmlns="http://www.w3.org/2005/Atom">John Doe</name>
       <email xmlns="http://www.w3.org/2005/Atom">johndoes@someemailadress.com</email>
       <uri xmlns="http://www.w3.org/2005/Atom">http://www.google.com</uri>
   </author>
"""

TEST_LINK = """<?xml version="1.0" encoding="utf-8"?>
   <link xmlns="http://www.w3.org/2005/Atom" href="http://www.google.com" 
       rel="test rel" foo1="bar" foo2="rab"/>
"""

TEST_GBASE_ATTRIBUTE = """<?xml version="1.0" encoding="utf-8"?>
   <g:brand type='text' xmlns:g="http://base.google.com/ns/1.0">Digital Camera Battery</g:brand>
"""
   

CALENDAR_FEED = """<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
xmlns:gd='http://schemas.google.com/g/2005'
xmlns:gCal='http://schemas.google.com/gCal/2005'>
  <id>http://www.google.com/calendar/feeds/default</id>
  <updated>2007-03-20T22:48:57.833Z</updated>
  <title type='text'>GData Ops Demo's Calendar List</title>
  <link rel='http://schemas.google.com/g/2005#feed'
  type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default'></link>
  <link rel='http://schemas.google.com/g/2005#post'
  type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default'></link>
  <link rel='self' type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default'></link>
  <author>
    <name>GData Ops Demo</name>
    <email>gdata.ops.demo@gmail.com</email>
  </author>
  <generator version='1.0' uri='http://www.google.com/calendar'>
  Google Calendar</generator>
  <openSearch:startIndex>1</openSearch:startIndex>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/gdata.ops.demo%40gmail.com</id>
    <published>2007-03-20T22:48:57.837Z</published>
    <updated>2007-03-20T22:48:52.000Z</updated>
    <title type='text'>GData Ops Demo</title>
    <link rel='alternate' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/gdata.ops.demo%40gmail.com/private/full'>
    </link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/gdata.ops.demo%40gmail.com'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:color value='#2952A3'></gCal:color>
    <gCal:accesslevel value='owner'></gCal:accesslevel>
    <gCal:hidden value='false'></gCal:hidden>
    <gCal:timezone value='America/Los_Angeles'></gCal:timezone>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/jnh21ovnjgfph21h32gvms2758%40group.calendar.google.com</id>
    <published>2007-03-20T22:48:57.837Z</published>
    <updated>2007-03-20T22:48:53.000Z</updated>
    <title type='text'>GData Ops Demo Secondary Calendar</title>
    <summary type='text'></summary>
    <link rel='alternate' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/jnh21ovnjgfph21h32gvms2758%40group.calendar.google.com/private/full'>
    </link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/jnh21ovnjgfph21h32gvms2758%40group.calendar.google.com'>
    </link>
    <author>
      <name>GData Ops Demo Secondary Calendar</name>
    </author>
    <gCal:color value='#528800'></gCal:color>
    <gCal:accesslevel value='owner'></gCal:accesslevel>
    <gCal:hidden value='false'></gCal:hidden>
    <gCal:timezone value='America/Los_Angeles'></gCal:timezone>
    <gd:where valueString=''></gd:where>
  </entry>
</feed>
"""

CALENDAR_FULL_EVENT_FEED = """<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
xmlns:gd='http://schemas.google.com/g/2005'
xmlns:gCal='http://schemas.google.com/gCal/2005'>
  <id>
  http://www.google.com/calendar/feeds/default/private/full</id>
  <updated>2007-03-20T21:29:57.000Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind'
  term='http://schemas.google.com/g/2005#event'></category>
  <title type='text'>GData Ops Demo</title>
  <subtitle type='text'>GData Ops Demo</subtitle>
  <link rel='http://schemas.google.com/g/2005#feed'
  type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default/private/full'>
  </link>
  <link rel='http://schemas.google.com/g/2005#post'
  type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default/private/full'>
  </link>
  <link rel='self' type='application/atom+xml'
  href='http://www.google.com/calendar/feeds/default/private/full?updated-min=2001-01-01&amp;max-results=25'>
  </link>
  <author>
    <name>GData Ops Demo</name>
    <email>gdata.ops.demo@gmail.com</email>
  </author>
  <generator version='1.0' uri='http://www.google.com/calendar'>
  Google Calendar</generator>
  <openSearch:totalResults>10</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>25</openSearch:itemsPerPage>
  <gCal:timezone value='America/Los_Angeles'></gCal:timezone>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/o99flmgmkfkfrr8u745ghr3100</id>
    <published>2007-03-20T21:29:52.000Z</published>
    <updated>2007-03-20T21:29:57.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>test deleted</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=bzk5ZmxtZ21rZmtmcnI4dTc0NWdocjMxMDAgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/o99flmgmkfkfrr8u745ghr3100'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/o99flmgmkfkfrr8u745ghr3100/63310109397'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.canceled'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/o99flmgmkfkfrr8u745ghr3100/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-23T12:00:00.000-07:00'
    endTime='2007-03-23T13:00:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/2qt3ao5hbaq7m9igr5ak9esjo0</id>
    <published>2007-03-20T21:26:04.000Z</published>
    <updated>2007-03-20T21:28:46.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Afternoon at Dolores Park with Kim</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=MnF0M2FvNWhiYXE3bTlpZ3I1YWs5ZXNqbzAgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/2qt3ao5hbaq7m9igr5ak9esjo0'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/2qt3ao5hbaq7m9igr5ak9esjo0/63310109326'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/2qt3ao5hbaq7m9igr5ak9esjo0/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.private'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:who rel='http://schemas.google.com/g/2005#event.organizer'
    valueString='GData Ops Demo' email='gdata.ops.demo@gmail.com'>
      <gd:attendeeStatus value='http://schemas.google.com/g/2005#event.accepted'>
      </gd:attendeeStatus>
    </gd:who>
    <gd:who rel='http://schemas.google.com/g/2005#event.attendee'
    valueString='Ryan Boyd (API)' email='api.rboyd@gmail.com'>
      <gd:attendeeStatus value='http://schemas.google.com/g/2005#event.invited'>
      </gd:attendeeStatus>
    </gd:who>
    <gd:when startTime='2007-03-24T12:00:00.000-07:00'
    endTime='2007-03-24T15:00:00.000-07:00'>
      <gd:reminder minutes='20'></gd:reminder>
    </gd:when>
    <gd:where valueString='Dolores Park with Kim'></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/uvsqhg7klnae40v50vihr1pvos</id>
    <published>2007-03-20T21:28:37.000Z</published>
    <updated>2007-03-20T21:28:37.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Team meeting</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=dXZzcWhnN2tsbmFlNDB2NTB2aWhyMXB2b3NfMjAwNzAzMjNUMTYwMDAwWiBnZGF0YS5vcHMuZGVtb0Bt'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/uvsqhg7klnae40v50vihr1pvos'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/uvsqhg7klnae40v50vihr1pvos/63310109317'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gd:recurrence>DTSTART;TZID=America/Los_Angeles:20070323T090000
    DTEND;TZID=America/Los_Angeles:20070323T100000
    RRULE:FREQ=WEEKLY;BYDAY=FR;UNTIL=20070817T160000Z;WKST=SU
    BEGIN:VTIMEZONE TZID:America/Los_Angeles
    X-LIC-LOCATION:America/Los_Angeles BEGIN:STANDARD
    TZOFFSETFROM:-0700 TZOFFSETTO:-0800 TZNAME:PST
    DTSTART:19701025T020000 RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
    END:STANDARD BEGIN:DAYLIGHT TZOFFSETFROM:-0800 TZOFFSETTO:-0700
    TZNAME:PDT DTSTART:19700405T020000
    RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU END:DAYLIGHT
    END:VTIMEZONE</gd:recurrence>
    <gCal:sendEventNotifications value='true'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:visibility value='http://schemas.google.com/g/2005#event.public'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:reminder minutes='10'></gd:reminder>
    <gd:where valueString=''></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/st4vk9kiffs6rasrl32e4a7alo</id>
    <published>2007-03-20T21:25:46.000Z</published>
    <updated>2007-03-20T21:25:46.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Movie with Kim and danah</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=c3Q0dms5a2lmZnM2cmFzcmwzMmU0YTdhbG8gZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/st4vk9kiffs6rasrl32e4a7alo'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/st4vk9kiffs6rasrl32e4a7alo/63310109146'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/st4vk9kiffs6rasrl32e4a7alo/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-24T20:00:00.000-07:00'
    endTime='2007-03-24T21:00:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/ofl1e45ubtsoh6gtu127cls2oo</id>
    <published>2007-03-20T21:24:43.000Z</published>
    <updated>2007-03-20T21:25:08.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Dinner with Kim and Sarah</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=b2ZsMWU0NXVidHNvaDZndHUxMjdjbHMyb28gZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/ofl1e45ubtsoh6gtu127cls2oo'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/ofl1e45ubtsoh6gtu127cls2oo/63310109108'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/ofl1e45ubtsoh6gtu127cls2oo/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-20T19:00:00.000-07:00'
    endTime='2007-03-20T21:30:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/b69s2avfi2joigsclecvjlc91g</id>
    <published>2007-03-20T21:24:19.000Z</published>
    <updated>2007-03-20T21:25:05.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Dinner with Jane and John</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=YjY5czJhdmZpMmpvaWdzY2xlY3ZqbGM5MWcgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/b69s2avfi2joigsclecvjlc91g'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/b69s2avfi2joigsclecvjlc91g/63310109105'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/b69s2avfi2joigsclecvjlc91g/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-22T17:00:00.000-07:00'
    endTime='2007-03-22T19:30:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/u9p66kkiotn8bqh9k7j4rcnjjc</id>
    <published>2007-03-20T21:24:33.000Z</published>
    <updated>2007-03-20T21:24:33.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Tennis with Elizabeth</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=dTlwNjZra2lvdG44YnFoOWs3ajRyY25qamMgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/u9p66kkiotn8bqh9k7j4rcnjjc'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/u9p66kkiotn8bqh9k7j4rcnjjc/63310109073'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/u9p66kkiotn8bqh9k7j4rcnjjc/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-24T10:00:00.000-07:00'
    endTime='2007-03-24T11:00:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/76oj2kceidob3s708tvfnuaq3c</id>
    <published>2007-03-20T21:24:00.000Z</published>
    <updated>2007-03-20T21:24:00.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>Lunch with Jenn</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=NzZvajJrY2VpZG9iM3M3MDh0dmZudWFxM2MgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/76oj2kceidob3s708tvfnuaq3c'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/76oj2kceidob3s708tvfnuaq3c/63310109040'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/76oj2kceidob3s708tvfnuaq3c/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-03-20T11:30:00.000-07:00'
    endTime='2007-03-20T12:30:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/5np9ec8m7uoauk1vedh5mhodco</id>
    <published>2007-03-20T07:50:02.000Z</published>
    <updated>2007-03-20T20:39:26.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>test entry</title>
    <content type='text'>test desc</content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=NW5wOWVjOG03dW9hdWsxdmVkaDVtaG9kY28gZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/5np9ec8m7uoauk1vedh5mhodco'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/5np9ec8m7uoauk1vedh5mhodco/63310106366'>
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/5np9ec8m7uoauk1vedh5mhodco/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.private'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:who rel='http://schemas.google.com/g/2005#event.attendee'
    valueString='Vivian Li' email='vli@google.com'>
      <gd:attendeeStatus value='http://schemas.google.com/g/2005#event.declined'>
      </gd:attendeeStatus>
    </gd:who>
    <gd:who rel='http://schemas.google.com/g/2005#event.organizer'
    valueString='GData Ops Demo' email='gdata.ops.demo@gmail.com'>
      <gd:attendeeStatus value='http://schemas.google.com/g/2005#event.accepted'>
      </gd:attendeeStatus>
    </gd:who>
    <gd:when startTime='2007-03-21T08:00:00.000-07:00'
    endTime='2007-03-21T09:00:00.000-07:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where valueString='anywhere'></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/fu6sl0rqakf3o0a13oo1i1a1mg</id>
    <published>2007-02-14T23:23:37.000Z</published>
    <updated>2007-02-14T23:25:30.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>test</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=ZnU2c2wwcnFha2YzbzBhMTNvbzFpMWExbWcgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/fu6sl0rqakf3o0a13oo1i1a1mg'>
    </link>
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/fu6sl0rqakf3o0a13oo1i1a1mg/63307178730'>
    </link>
    <link rel="http://schemas.google.com/gCal/2005/webContent" title="World Cup" href="http://www.google.com/calendar/images/google-holiday.gif" type="image/gif">
      <gCal:webContent width="276" height="120" url="http://www.google.com/logos/worldcup06.gif" />
    </link>
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/fu6sl0rqakf3o0a13oo1i1a1mg/comments'>
      </gd:feedLink>
    </gd:comments>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:when startTime='2007-02-15T08:30:00.000-08:00'
    endTime='2007-02-15T09:30:00.000-08:00'>
      <gd:reminder minutes='10'></gd:reminder>
    </gd:when>
    <gd:where></gd:where>
  </entry>
  <entry>
    <id>
    http://www.google.com/calendar/feeds/default/private/full/h7a0haa4da8sil3rr19ia6luvc</id>
    <published>2007-07-16T22:13:28.000Z</published>
    <updated>2007-07-16T22:13:29.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event' />
    <title type='text'></title>
    <content type='text' />
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=aDdhMGhhYTRkYThzaWwzcnIxOWlhNmx1dmMgZ2RhdGEub3BzLmRlbW9AbQ'
    title='alternate' />
    <link rel='http://schemas.google.com/gCal/2005/webContent'
    type='application/x-google-gadgets+xml'
    href='http://gdata.ops.demo.googlepages.com/birthdayicon.gif'
    title='Date and Time Gadget'>
      <gCal:webContent width='300' height='136'
      url='http://google.com/ig/modules/datetime.xml'>
        <gCal:webContentGadgetPref name='color' value='green' />
      </gCal:webContent>
    </link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/h7a0haa4da8sil3rr19ia6luvc' />
    <link rel='edit' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/full/h7a0haa4da8sil3rr19ia6luvc/63320307209' />
    <author>
      <name>GData Ops Demo</name>
      <email>gdata.ops.demo@gmail.com</email>
    </author>
    <gd:comments>
      <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/h7a0haa4da8sil3rr19ia6luvc/comments' />
    </gd:comments>
    <gCal:sendEventNotifications value='false'>
    </gCal:sendEventNotifications>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed' />
    <gd:visibility value='http://schemas.google.com/g/2005#event.default' />
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque' />
    <gd:when startTime='2007-03-14' endTime='2007-03-15' />
    <gd:where />
  </entry>
</feed>
"""

CALENDAR_BATCH_REQUEST = """<?xml version='1.0' encoding='utf-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' 
      xmlns:batch='http://schemas.google.com/gdata/batch'
      xmlns:gCal='http://schemas.google.com/gCal/2005'>
  <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
  <entry>
    <batch:id>1</batch:id>
    <batch:operation type='insert' />
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event inserted via batch</title>
  </entry>
  <entry>
    <batch:id>2</batch:id>
    <batch:operation type='query' />
    <id>http://www.google.com/calendar/feeds/default/private/full/glcs0kv2qqa0gf52qi1jo018gc</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event queried via batch</title>
  </entry>
  <entry>
    <batch:id>3</batch:id>
    <batch:operation type='update' />
    <id>http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event updated via batch</title>
    <link rel='alternate' type='text/html' 
        href='http://www.google.com/calendar/event?eid=dWptMGdvNWR0bmdka3I2dTkxZGNxdmowcXMgaGFyaXNodi50ZXN0QG0' title='alternate' />
    <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs' />
    <link rel='edit' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs/63326098791' />
  </entry>
  <entry>
    <batch:id>4</batch:id>
    <batch:operation type='delete' />
    <id>http://www.google.com/calendar/feeds/default/private/full/d8qbg9egk1n6lhsgq1sjbqffqc</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event deleted via batch</title>
    <link rel='alternate' type='text/html' 
        href='http://www.google.com/calendar/event?eid=ZDhxYmc5ZWdrMW42bGhzZ3Exc2picWZmcWMgaGFyaXNodi50ZXN0QG0' title='alternate' />
    <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/d8qbg9egk1n6lhsgq1sjbqffqc' />
    <link rel='edit' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/d8qbg9egk1n6lhsgq1sjbqffqc/63326018324' />
  </entry>
</feed>
"""

CALENDAR_BATCH_RESPONSE = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' 
      xmlns:batch='http://schemas.google.com/gdata/batch'
      xmlns:gCal='http://schemas.google.com/gCal/2005'>
  <id>http://www.google.com/calendar/feeds/default/private/full</id>
  <updated>2007-09-21T23:01:00.380Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event'></category>
  <title type='text'>Batch Feed</title>
  <link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' 
      href='http://www.google.com/calendar/feeds/default/private/full' />
  <link rel='http://schemas.google.com/g/2005#post' type='application/atom+xml' 
      href='http://www.google.com/calendar/feeds/default/private/full' />
  <link rel='http://schemas.google.com/g/2005#batch' type='application/atom+xml' 
      href='http://www.google.com/calendar/feeds/default/private/full/batch' />
  <entry>
    <batch:id>1</batch:id>
    <batch:status code='201' reason='Created' />
    <batch:operation type='insert' />
    <id>http://www.google.com/calendar/feeds/default/private/full/n9ug78gd9tv53ppn4hdjvk68ek</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event inserted via batch</title>
    <link rel='alternate' type='text/html' 
        href='http://www.google.com/calendar/event?eid=bjl1Zzc4Z2Q5dHY1M3BwbjRoZGp2azY4ZWsgaGFyaXNodi50ZXN0QG0' title='alternate' />
    <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/n9ug78gd9tv53ppn4hdjvk68ek' />
    <link rel='edit' type='application/atom+xml' 
      href='http://www.google.com/calendar/feeds/default/private/full/n9ug78gd9tv53ppn4hdjvk68ek/63326098860' />
  </entry>
  <entry>
    <batch:id>2</batch:id>
    <batch:status code='200' reason='Success' />
    <batch:operation type='query' />
    <id>http://www.google.com/calendar/feeds/default/private/full/glsc0kv2aqa0ff52qi1jo018gc</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event queried via batch</title>
    <link rel='alternate' type='text/html' 
        href='http://www.google.com/calendar/event?eid=Z2xzYzBrdjJhcWEwZmY1MnFpMWpvMDE4Z2MgaGFyaXNodi50ZXN0QG0' title='alternate' />
    <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/glsc0kv2aqa0ff52qi1jo018gc' />
    <link rel='edit' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/glsc0kv2aqa0ff52qi1jo018gc/63326098791' />
  </entry>
  <entry xmlns:gCal='http://schemas.google.com/gCal/2005'>
    <batch:id>3</batch:id>
    <batch:status code='200' reason='Success' />
    <batch:operation type='update' />
    <id>http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event updated via batch</title>
    <link rel='alternate' type='text/html' 
        href='http://www.google.com/calendar/event?eid=dWptMGdvNWR0bmdka3I2dTkxZGNxdmowcXMgaGFyaXNodi50ZXN0QG0' title='alternate' />
    <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs' />
    <link rel='edit' type='application/atom+xml' 
        href='http://www.google.com/calendar/feeds/default/private/full/ujm0go5dtngdkr6u91dcqvj0qs/63326098860' />
    <batch:id>3</batch:id>
    <batch:status code='200' reason='Success' />
    <batch:operation type='update' />
  </entry>
  <entry>
    <batch:id>4</batch:id>
    <batch:status code='200' reason='Success' />
    <batch:operation type='delete' />
    <id>http://www.google.com/calendar/feeds/default/private/full/d8qbg9egk1n6lhsgq1sjbqffqc</id>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/g/2005#event' />
    <title type='text'>Event deleted via batch</title>
    <content type='text'>Deleted</content>
  </entry>
</feed>
"""

GBASE_ATTRIBUTE_FEED = """<?xml version='1.0' encoding='UTF-8'?>
    <feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gm='http://base.google.com/ns-metadata/1.0'>
      <id>http://www.google.com/base/feeds/attributes</id>
      <updated>2006-11-01T20:35:59.578Z</updated>
      <category scheme='http://base.google.com/categories/itemtypes' term='online jobs'></category>
      <category scheme='http://base.google.com/categories/itemtypes' term='jobs'></category>
      <title type='text'>Attribute histogram for query: [item type:jobs]</title>
      <link rel='alternate' type='text/html' href='http://base.google.com'></link>
      <link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://www.google.com/base/feeds
/attributes'></link>
      <link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/attributes/-/jobs'></link>
      <generator version='1.0' uri='http://base.google.com'>GoogleBase</generator>
      <openSearch:totalResults>16</openSearch:totalResults>
      <openSearch:startIndex>1</openSearch:startIndex>
      <openSearch:itemsPerPage>16</openSearch:itemsPerPage>
      <entry>
        <id>http://www.google.com/base/feeds/attributes/job+industry%28text%29N%5Bitem+type%3Ajobs%5D</id>
        <updated>2006-11-01T20:36:00.100Z</updated>
        <title type='text'>job industry(text)</title>
        <content type='text'>Attribute"job industry" of type text.
        </content>
        <link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/attributes/job+industry%28text
%29N%5Bitem+type%3Ajobs%5D'></link>
        <gm:attribute name='job industry' type='text' count='4416629'>
          <gm:value count='380772'>it internet</gm:value>
          <gm:value count='261565'>healthcare</gm:value>
          <gm:value count='142018'>information technology</gm:value>
          <gm:value count='124622'>accounting</gm:value>
          <gm:value count='111311'>clerical and administrative</gm:value>
          <gm:value count='82928'>other</gm:value>
          <gm:value count='77620'>sales and sales management</gm:value>
          <gm:value count='68764'>information systems</gm:value>
          <gm:value count='65859'>engineering and architecture</gm:value>
          <gm:value count='64757'>sales</gm:value>
        </gm:attribute>
      </entry>
    </feed>
"""


GBASE_ATTRIBUTE_ENTRY = """<?xml version='1.0' encoding='UTF-8'?>
 <entry xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gm='http://base.google.com/ns-metadata/1.0'>
        <id>http://www.google.com/base/feeds/attributes/job+industry%28text%29N%5Bitem+type%3Ajobs%5D</id>
        <updated>2006-11-01T20:36:00.100Z</updated>
        <title type='text'>job industry(text)</title>
        <content type='text'>Attribute"job industry" of type text.
        </content>
        <link rel='self' type='application/atom+xml' href='http://www.google.com/base/feeds/attributes/job+industry%28text%29N%5Bitem+type%3Ajobs%5D'></link>
        <gm:attribute name='job industry' type='text' count='4416629'>
          <gm:value count='380772'>it internet</gm:value>
          <gm:value count='261565'>healthcare</gm:value>
          <gm:value count='142018'>information technology</gm:value>
          <gm:value count='124622'>accounting</gm:value>
          <gm:value count='111311'>clerical and administrative</gm:value>
          <gm:value count='82928'>other</gm:value>
          <gm:value count='77620'>sales and sales management</gm:value>
          <gm:value count='68764'>information systems</gm:value>
          <gm:value count='65859'>engineering and architecture</gm:value>
          <gm:value count='64757'>sales</gm:value>
        </gm:attribute>
      </entry>
""" 

GBASE_LOCALES_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
      xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
      xmlns:gm='http://base.google.com/ns-metadata/1.0'>
         <id> http://www.google.com/base/feeds/locales/</id>
  <updated>2006-06-13T18:11:40.120Z</updated>
  <title type="text">Locales</title> 
  <link rel="alternate" type="text/html" href="http://base.google.com"/>
  <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml"

       href="http://www.google.com/base/feeds/locales/"/>
  <link rel="self" type="application/atom+xml" href="http://www.google.com/base/feeds/locales/"/>
         <author>
    <name>Google Inc.</name>
    <email>base@google.com</email>
  </author>
  <generator version="1.0" uri="http://base.google.com">GoogleBase</generator>
  <openSearch:totalResults>3</openSearch:totalResults>
  <openSearch:itemsPerPage>25</openSearch:itemsPerPage>

<entry>
  <id>http://www.google.com/base/feeds/locales/en_US</id>
  <updated>2006-03-27T22:27:36.658Z</updated>
  <category scheme="http://base.google.com/categories/locales" term="en_US"/>

  <title type="text">en_US</title>
  <content type="text">en_US</content>
  <link rel="self" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/locales/en_US"></link>

  <link rel="related" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/itemtypes/en_US" title="Item types in en_US"/>
</entry>
<entry>
         <id>http://www.google.com/base/feeds/locales/en_GB</id>
  <updated>2006-06-13T18:14:18.601Z</updated>
  <category scheme="http://base.google.com/categories/locales" term="en_GB"/>
  <title type="text">en_GB</title>
  <content type="text">en_GB</content>
  <link rel="related" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/itemtypes/en_GB" title="Item types in en_GB"/>
  <link rel="self" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/locales/en_GB"/>
</entry>
<entry>
  <id>http://www.google.com/base/feeds/locales/de_DE</id>
  <updated>2006-06-13T18:14:18.601Z</updated>
  <category scheme="http://base.google.com/categories/locales" term="de_DE"/>
  <title type="text">de_DE</title>
  <content type="text">de_DE</content>
  <link rel="related" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/itemtypes/de_DE" title="Item types in de_DE"/>
  <link rel="self" type="application/atom+xml" 
     href="http://www.google.com/base/feeds/locales/de_DE"/>
</entry>
</feed>"""

GBASE_STRING_ENCODING_ENTRY = """<?xml version='1.0' encoding='UTF-8'?>
<entry xmlns='http://www.w3.org/2005/Atom' xmlns:gm='http://base.google.com/ns-metadata/1.0' 
       xmlns:g='http://base.google.com/ns/1.0' xmlns:batch='http://schemas.google.com/gdata/batch'>
  <id>http://www.google.com/base/feeds/snippets/17495780256183230088</id>
  <published>2007-12-09T03:13:07.000Z</published>
  <updated>2008-01-07T03:26:46.000Z</updated>
  <category scheme='http://base.google.com/categories/itemtypes' term='Products'/>
  <title type='text'>Digital Camera Cord Fits SONY Cybershot DSC-R1 S40</title>
  <content type='html'>SONY \xC2\xB7 Cybershot Digital Camera Usb Cable DESCRIPTION 
      This is a 2.5 USB 2.0 A to Mini B (5 Pin) high quality digital camera 
      cable used for connecting your Sony Digital Cameras and Camcoders. Backward 
      Compatible with USB 2.0, 1.0 and 1.1. Fully  ...</content>
  <link rel='alternate' type='text/html' 
        href='http://adfarm.mediaplex.com/ad/ck/711-5256-8196-2?loc=http%3A%2F%2Fcgi.ebay.com%2FDigital-Camera-Cord-Fits-SONY-Cybershot-DSC-R1-S40_W0QQitemZ270195049057QQcmdZViewItem'/>
  <link rel='self' type='application/atom+xml' 
        href='http://www.google.com/base/feeds/snippets/17495780256183230088'/>
  <author>
    <name>eBay</name>
  </author>
  <g:item_type type='text'>Products</g:item_type>
  <g:item_language type='text'>EN</g:item_language>
  <g:target_country type='text'>US</g:target_country>
  <g:price type='floatUnit'>0.99 usd</g:price>
  <g:image_link type='url'>http://thumbs.ebaystatic.com/pict/270195049057_1.jpg</g:image_link>
  <g:category type='text'>Cameras &amp; Photo&gt;Digital Camera Accessories&gt;Cables</g:category>
  <g:category type='text'>Cords &amp; Connectors&gt;USB Cables&gt;For Other Brands</g:category>
  <g:customer_id type='int'>11729</g:customer_id>
  <g:id type='text'>270195049057</g:id>
  <g:expiration_date type='dateTime'>2008-02-06T03:26:46Z</g:expiration_date>
</entry>"""


RECURRENCE_EXCEPTION_ENTRY = """<entry xmlns='http://www.w3.org/2005/Atom'
xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
xmlns:gd='http://schemas.google.com/g/2005'
xmlns:gCal='http://schemas.google.com/gCal/2005'>
    <id>
    http://www.google.com/calendar/feeds/default/private/composite/i7lgfj69mjqjgnodklif3vbm7g</id>
    <published>2007-04-05T21:51:49.000Z</published>
    <updated>2007-04-05T21:51:49.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/g/2005#event'></category>
    <title type='text'>testDavid</title>
    <content type='text'></content>
    <link rel='alternate' type='text/html'
    href='http://www.google.com/calendar/event?eid=aTdsZ2ZqNjltanFqZ25vZGtsaWYzdmJtN2dfMjAwNzA0MDNUMTgwMDAwWiBnZGF0YS5vcHMudGVzdEBt'
    title='alternate'></link>
    <link rel='self' type='application/atom+xml'
    href='http://www.google.com/calendar/feeds/default/private/composite/i7lgfj69mjqjgnodklif3vbm7g'>
    </link>
    <author>
      <name>gdata ops</name>
      <email>gdata.ops.test@gmail.com</email>
    </author>
    <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
    </gd:visibility>
    <gCal:sendEventNotifications value='true'>
    </gCal:sendEventNotifications>
    <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
    </gd:transparency>
    <gd:eventStatus value='http://schemas.google.com/g/2005#event.confirmed'>
    </gd:eventStatus>
    <gd:recurrence>DTSTART;TZID=America/Anchorage:20070403T100000
    DTEND;TZID=America/Anchorage:20070403T110000
    RRULE:FREQ=DAILY;UNTIL=20070408T180000Z;WKST=SU
    EXDATE;TZID=America/Anchorage:20070407T100000
    EXDATE;TZID=America/Anchorage:20070405T100000
    EXDATE;TZID=America/Anchorage:20070404T100000 BEGIN:VTIMEZONE
    TZID:America/Anchorage X-LIC-LOCATION:America/Anchorage
    BEGIN:STANDARD TZOFFSETFROM:-0800 TZOFFSETTO:-0900 TZNAME:AKST
    DTSTART:19701025T020000 RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
    END:STANDARD BEGIN:DAYLIGHT TZOFFSETFROM:-0900 TZOFFSETTO:-0800
    TZNAME:AKDT DTSTART:19700405T020000
    RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU END:DAYLIGHT
    END:VTIMEZONE</gd:recurrence>
    <gd:where valueString=''></gd:where>
    <gd:reminder minutes='10'></gd:reminder>
    <gd:recurrenceException specialized='true'>
      <gd:entryLink>
        <entry>
          <id>i7lgfj69mjqjgnodklif3vbm7g_20070407T180000Z</id>
          <published>2007-04-05T21:51:49.000Z</published>
          <updated>2007-04-05T21:52:58.000Z</updated>
          <category scheme='http://schemas.google.com/g/2005#kind'
          term='http://schemas.google.com/g/2005#event'></category>
          <title type='text'>testDavid</title>
          <content type='text'></content>
          <link rel='alternate' type='text/html'
          href='http://www.google.com/calendar/event?eid=aTdsZ2ZqNjltanFqZ25vZGtsaWYzdmJtN2dfMjAwNzA0MDdUMTgwMDAwWiBnZGF0YS5vcHMudGVzdEBt'
          title='alternate'></link>
          <author>
            <name>gdata ops</name>
            <email>gdata.ops.test@gmail.com</email>
          </author>
          <gd:visibility value='http://schemas.google.com/g/2005#event.default'>
          </gd:visibility>
          <gd:originalEvent id='i7lgfj69mjqjgnodklif3vbm7g'
          href='http://www.google.com/calendar/feeds/default/private/composite/i7lgfj69mjqjgnodklif3vbm7g'>

            <gd:when startTime='2007-04-07T13:00:00.000-05:00'>
            </gd:when>
          </gd:originalEvent>
          <gCal:sendEventNotifications value='false'>
          </gCal:sendEventNotifications>
          <gd:transparency value='http://schemas.google.com/g/2005#event.opaque'>
          </gd:transparency>
          <gd:eventStatus value='http://schemas.google.com/g/2005#event.canceled'>
          </gd:eventStatus>
          <gd:comments>
            <gd:feedLink href='http://www.google.com/calendar/feeds/default/private/full/i7lgfj69mjqjgnodklif3vbm7g_20070407T180000Z/comments'>

              <feed>
                <updated>2007-04-05T21:54:09.285Z</updated>
                <category scheme='http://schemas.google.com/g/2005#kind'
                term='http://schemas.google.com/g/2005#message'>
                </category>
                <title type='text'>Comments for: testDavid</title>
                <link rel='alternate' type='text/html'
                href='http://www.google.com/calendar/feeds/default/private/full/i7lgfj69mjqjgnodklif3vbm7g_20070407T180000Z/comments'
                title='alternate'></link>
              </feed>
            </gd:feedLink>
          </gd:comments>
          <gd:when startTime='2007-04-07T13:00:00.000-05:00'
          endTime='2007-04-07T14:00:00.000-05:00'>
            <gd:reminder minutes='10'></gd:reminder>
          </gd:when>
          <gd:where valueString=''></gd:where>
        </entry>
      </gd:entryLink>
    </gd:recurrenceException>
  </entry>"""

NICK_ENTRY = """<?xml version="1.0" encoding="UTF-8"?>
<atom:entry xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:apps="http://schemas.google.com/apps/2006"
  xmlns:gd="http://schemas.google.com/g/2005">
  <atom:id>https://www.google.com/a/feeds/example.com/nickname/2.0/Foo</atom:id>
  <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
  <atom:category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/apps/2006#nickname'/>
  <atom:title type="text">Foo</atom:title>
  <atom:link rel="self" type="application/atom+xml"
    href="https://www.google.com/a/feeds/example.com/nickname/2.0/Foo"/>
  <atom:link rel="edit" type="application/atom+xml"
    href="https://www.google.com/a/feeds/example.com/nickname/2.0/Foo"/>
  <apps:nickname name="Foo"/>
  <apps:login userName="TestUser"/>
</atom:entry>"""

NICK_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<atom:feed xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:apps="http://schemas.google.com/apps/2006">
  <atom:id>
    http://www.google.com/a/feeds/example.com/nickname/2.0
  </atom:id>
  <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
  <atom:category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/apps/2006#nickname'/>
  <atom:title type="text">Nicknames for user SusanJones</atom:title>
  <atom:link rel='http://schemas.google.com/g/2005#feed'
    type="application/atom+xml"
    href="http://www.google.com/a/feeds/example.com/nickname/2.0"/>
  <atom:link rel='http://schemas.google.com/g/2005#post'
    type="application/atom+xml"
    href="http://www.google.com/a/feeds/example.com/nickname/2.0"/>
  <atom:link rel="self" type="application/atom+xml"
    href="http://www.google.com/a/feeds/example.com/nickname/2.0?username=TestUser"/>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>2</openSearch:itemsPerPage>
  <atom:entry>
    <atom:id>
      http://www.google.com/a/feeds/example.com/nickname/2.0/Foo
    </atom:id>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
      term='http://schemas.google.com/apps/2006#nickname'/>
    <atom:title type="text">Foo</atom:title>
    <atom:link rel="self" type="application/atom+xml"
      href="http://www.google.com/a/feeds/example.com/nickname/2.0/Foo"/>
    <atom:link rel="edit" type="application/atom+xml"
      href="http://www.google.com/a/feeds/example.com/nickname/2.0/Foo"/>
    <apps:nickname name="Foo"/>
    <apps:login userName="TestUser"/>
  </atom:entry>
  <atom:entry>
    <atom:id>
      http://www.google.com/a/feeds/example.com/nickname/2.0/suse
    </atom:id>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
      term='http://schemas.google.com/apps/2006#nickname'/>
    <atom:title type="text">suse</atom:title>
    <atom:link rel="self" type="application/atom+xml"
      href="http://www.google.com/a/feeds/example.com/nickname/2.0/Bar"/>
    <atom:link rel="edit" type="application/atom+xml"
      href="http://www.google.com/a/feeds/example.com/nickname/2.0/Bar"/>
    <apps:nickname name="Bar"/>
    <apps:login userName="TestUser"/>
  </atom:entry>
</atom:feed>"""

USER_ENTRY = """<?xml version="1.0" encoding="UTF-8"?>
<atom:entry xmlns:atom="http://www.w3.org/2005/Atom"
            xmlns:apps="http://schemas.google.com/apps/2006"
            xmlns:gd="http://schemas.google.com/g/2005">
  <atom:id>https://www.google.com/a/feeds/example.com/user/2.0/TestUser</atom:id>
  <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
  <atom:category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/apps/2006#user'/>
  <atom:title type="text">TestUser</atom:title>
  <atom:link rel="self" type="application/atom+xml"
    href="https://www.google.com/a/feeds/example.com/user/2.0/TestUser"/>
  <atom:link rel="edit" type="application/atom+xml"
    href="https://www.google.com/a/feeds/example.com/user/2.0/TestUser"/>
  <apps:login userName="TestUser" password="password" suspended="false"
    ipWhitelisted='false' hashFunctionName="SHA-1"/>
  <apps:name familyName="Test" givenName="User"/>
  <apps:quota limit="1024"/>
  <gd:feedLink rel='http://schemas.google.com/apps/2006#user.nicknames'
    href="https://www.google.com/a/feeds/example.com/nickname/2.0?username=Test-3121"/>
  <gd:feedLink rel='http://schemas.google.com/apps/2006#user.emailLists'
    href="https://www.google.com/a/feeds/example.com/emailList/2.0?recipient=testlist@example.com"/>
</atom:entry>"""

USER_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<atom:feed xmlns:atom="http://www.w3.org/2005/Atom" 
  xmlns:apps="http://schemas.google.com/apps/2006"
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:gd="http://schemas.google.com/g/2005">
    <atom:id>
        http://www.google.com/a/feeds/example.com/user/2.0
    </atom:id>
    <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
    <atom:category scheme='http://schemas.google.com/g/2005#kind' 
        term='http://schemas.google.com/apps/2006#user'/>
    <atom:title type="text">Users</atom:title>
    <atom:link rel="next" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/user/2.0?startUsername=john"/>
    <atom:link rel='http://schemas.google.com/g/2005#feed' 
        type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/user/2.0"/>
    <atom:link rel='http://schemas.google.com/g/2005#post'
        type="application/atom+xml"
        href="http://www.google.com/a/feeds/example.com/user/2.0"/>
    <atom:link rel="self" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/user/2.0"/>
    <openSearch:startIndex>1</openSearch:startIndex>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/user/2.0/TestUser
        </atom:id>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#user'/>
        <atom:title type="text">TestUser</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/user/2.0/TestUser"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/user/2.0/TestUser"/>
        <gd:who rel='http://schemas.google.com/apps/2006#user.recipient' 
            email="TestUser@example.com"/>
        <apps:login userName="TestUser" suspended="false"/>
        <apps:quota limit="2048"/>
        <apps:name familyName="Test" givenName="User"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#user.nicknames'
            href="http://www.google.com/a/feeds/example.com/nickname/2.0?username=TestUser"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#user.emailLists'
            href="http://www.google.com/a/feeds/example.com/emailList/2.0?recipient=TestUser@example.com"/>
    </atom:entry>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/user/2.0/JohnSmith
        </atom:id>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#user'/>
        <atom:title type="text">JohnSmith</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/user/2.0/JohnSmith"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/user/2.0/JohnSmith"/>
        <gd:who rel='http://schemas.google.com/apps/2006#user.recipient'
            email="JohnSmith@example.com"/>
        <apps:login userName="JohnSmith" suspended="false"/>
        <apps:quota limit="2048"/>
        <apps:name familyName="Smith" givenName="John"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#user.nicknames'
            href="http://www.google.com/a/feeds/example.com/nickname/2.0?username=JohnSmith"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#user.emailLists'
            href="http://www.google.com/a/feeds/example.com/emailList/2.0?recipient=JohnSmith@example.com"/>
    </atom:entry>
</atom:feed>"""

EMAIL_LIST_ENTRY = """<?xml version="1.0" encoding="UTF-8"?>
<atom:entry xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:apps="http://schemas.google.com/apps/2006"
  xmlns:gd="http://schemas.google.com/g/2005">
    <atom:id>
      https://www.google.com/a/feeds/example.com/emailList/2.0/testlist
    </atom:id>
    <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
      term='http://schemas.google.com/apps/2006#emailList'/>
    <atom:title type="text">testlist</atom:title>
    <atom:link rel="self" type="application/atom+xml" 
      href="https://www.google.com/a/feeds/example.com/emailList/2.0/testlist"/>
    <atom:link rel="edit" type="application/atom+xml" 
      href="https://www.google.com/a/feeds/example.com/emailList/2.0/testlist"/>
    <apps:emailList name="testlist"/>
    <gd:feedLink rel='http://schemas.google.com/apps/2006#emailList.recipients'
        href="http://www.google.com/a/feeds/example.com/emailList/2.0/testlist/recipient/"/>
</atom:entry>"""

EMAIL_LIST_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<atom:feed xmlns:atom="http://www.w3.org/2005/Atom" 
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:apps="http://schemas.google.com/apps/2006"
  xmlns:gd="http://schemas.google.com/g/2005">
    <atom:id>
        http://www.google.com/a/feeds/example.com/emailList/2.0
    </atom:id>
    <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
        term='http://schemas.google.com/apps/2006#emailList'/>
    <atom:title type="text">EmailLists</atom:title>
    <atom:link rel="next" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0?startEmailListName=john"/>
    <atom:link rel='http://schemas.google.com/g/2005#feed'
        type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0"/>
    <atom:link rel='http://schemas.google.com/g/2005#post' 
        type="application/atom+xml"
        href="http://www.google.com/a/feeds/example.com/emailList/2.0"/>
    <atom:link rel="self" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0"/>
    <openSearch:startIndex>1</openSearch:startIndex>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales
        </atom:id>
        <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#emailList'/>
        <atom:title type="text">us-sales</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales"/>
        <apps:emailList name="us-sales"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#emailList.recipients'
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/"/>
    </atom:entry>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/emailList/2.0/us-eng
        </atom:id>
        <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#emailList'/>
        <atom:title type="text">us-eng</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-eng"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-eng"/>
        <apps:emailList name="us-eng"/>
        <gd:feedLink rel='http://schemas.google.com/apps/2006#emailList.recipients'
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-eng/recipient/"/>
    </atom:entry>
</atom:feed>"""

EMAIL_LIST_RECIPIENT_ENTRY = """<?xml version="1.0" encoding="UTF-8"?>
<atom:entry xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:apps="http://schemas.google.com/apps/2006"
  xmlns:gd="http://schemas.google.com/g/2005">
    <atom:id>https://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/TestUser%40example.com</atom:id>
    <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
        term='http://schemas.google.com/apps/2006#emailList.recipient'/>
    <atom:title type="text">TestUser</atom:title>
    <atom:link rel="self" type="application/atom+xml" 
        href="https://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/TestUser%40example.com"/>
    <atom:link rel="edit" type="application/atom+xml" 
        href="https://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/TestUser%40example.com"/>
    <gd:who email="TestUser@example.com"/>
</atom:entry>"""

EMAIL_LIST_RECIPIENT_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<atom:feed xmlns:atom="http://www.w3.org/2005/Atom" 
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:gd="http://schemas.google.com/g/2005">
    <atom:id>
        http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient
    </atom:id>
    <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
    <atom:category scheme='http://schemas.google.com/g/2005#kind'
        term='http://schemas.google.com/apps/2006#emailList.recipient'/>
    <atom:title type="text">Recipients for email list us-sales</atom:title>
    <atom:link rel="next" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/?startRecipient=terry@example.com"/>
    <atom:link rel='http://schemas.google.com/g/2005#feed'
        type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient"/>
    <atom:link rel='http://schemas.google.com/g/2005#post'
        type="application/atom+xml"
        href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient"/>
    <atom:link rel="self" type="application/atom+xml" 
        href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient"/>
    <openSearch:startIndex>1</openSearch:startIndex>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/joe%40example.com
        </atom:id>
        <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#emailList.recipient'/>
        <atom:title type="text">joe@example.com</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/joe%40example.com"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/joe%40example.com"/>
        <gd:who email="joe@example.com"/>
    </atom:entry>
    <atom:entry>
        <atom:id>
            http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/susan%40example.com
        </atom:id>
        <atom:updated>1970-01-01T00:00:00.000Z</atom:updated>
        <atom:category scheme='http://schemas.google.com/g/2005#kind'
            term='http://schemas.google.com/apps/2006#emailList.recipient'/>
        <atom:title type="text">susan@example.com</atom:title>
        <atom:link rel="self" type="application/atom+xml" 
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/susan%40example.com"/>
        <atom:link rel="edit" type="application/atom+xml"
            href="http://www.google.com/a/feeds/example.com/emailList/2.0/us-sales/recipient/susan%40example.com"/>
        <gd:who email="susan@example.com"/>
    </atom:entry>
</atom:feed>"""

ACL_FEED = """<?xml version='1.0' encoding='UTF-8'?>
  <feed xmlns='http://www.w3.org/2005/Atom'
      xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
      xmlns:gAcl='http://schemas.google.com/acl/2007'>
    <id>http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full</id>
    <updated>2007-04-21T00:52:04.000Z</updated>
    <title type='text'>Elizabeth Bennet's access control list</title>
    <link rel='http://schemas.google.com/acl/2007#controlledObject'
      type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/private/full'>
    </link>
    <link rel='http://schemas.google.com/g/2005#feed'
      type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full'>
    </link>
    <link rel='http://schemas.google.com/g/2005#post'
      type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full'>
    </link>
    <link rel='self' type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full'>
    </link>
    <generator version='1.0'
      uri='http://www.google.com/calendar'>Google Calendar</generator>
    <openSearch:totalResults>2</openSearch:totalResults>
    <openSearch:startIndex>1</openSearch:startIndex>
    <entry>
      <id>http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com</id>
      <updated>2007-04-21T00:52:04.000Z</updated>
      <category scheme='http://schemas.google.com/g/2005#kind'
        term='http://schemas.google.com/acl/2007#accessRule'>
      </category>
      <title type='text'>owner</title>
      <content type='text'></content>
      <link rel='self' type='application/atom+xml'
        href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com'>
      </link>
      <link rel='edit' type='application/atom+xml'
        href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com'>
      </link>
      <author>
        <name>Elizabeth Bennet</name>
        <email>liz@gmail.com</email>
      </author>
      <gAcl:scope type='user' value='liz@gmail.com'></gAcl:scope>
      <gAcl:role value='http://schemas.google.com/gCal/2005#owner'>
      </gAcl:role>
    </entry>
    <entry>
      <id>http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/default</id>
      <updated>2007-04-21T00:52:04.000Z</updated>
      <category scheme='http://schemas.google.com/g/2005#kind'
        term='http://schemas.google.com/acl/2007#accessRule'>
      </category>
      <title type='text'>read</title>
      <content type='text'></content>
      <link rel='self' type='application/atom+xml'
        href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/default'>
      </link>
      <link rel='edit' type='application/atom+xml'
        href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/default'>
      </link>
      <author>
        <name>Elizabeth Bennet</name>
        <email>liz@gmail.com</email>
      </author>
      <gAcl:scope type='default'></gAcl:scope>
      <gAcl:role value='http://schemas.google.com/gCal/2005#read'>
      </gAcl:role>
    </entry>
  </feed>"""

ACL_ENTRY = """<?xml version='1.0' encoding='UTF-8'?>
  <entry xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gd='http://schemas.google.com/g/2005' xmlns:gCal='http://schemas.google.com/gCal/2005' xmlns:gAcl='http://schemas.google.com/acl/2007'>
    <id>http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com</id>
    <updated>2007-04-21T00:52:04.000Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
      term='http://schemas.google.com/acl/2007#accessRule'>
    </category>
    <title type='text'>owner</title>
    <content type='text'></content>
    <link rel='self' type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com'>
    </link>
    <link rel='edit' type='application/atom+xml'
      href='http://www.google.com/calendar/feeds/liz%40gmail.com/acl/full/user%3Aliz%40gmail.com'>
    </link>
    <author>
      <name>Elizabeth Bennet</name>
      <email>liz@gmail.com</email>
    </author>
    <gAcl:scope type='user' value='liz@gmail.com'></gAcl:scope>
    <gAcl:role value='http://schemas.google.com/gCal/2005#owner'>
    </gAcl:role>
  </entry>"""

DOCUMENT_LIST_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom"><ns1:totalResults
xmlns:ns1="http://a9.com/-/spec/opensearchrss/1.0/">2</ns1:totalResults><ns1:startIndex
xmlns:ns1="http://a9.com/-/spec/opensearchrss/1.0/">1</ns1:startIndex><ns0:entry><ns0:content
src="http://foo.com/fm?fmcmd=102&amp;key=supercalifragilisticexpeadocious"
type="text/html"
/><ns0:author><ns0:name>test.user</ns0:name><ns0:email>test.user@gmail.com</ns0:email></ns0:author><ns0:category
label="spreadsheet" scheme="http://schemas.google.com/g/2005#kind"
term="http://schemas.google.com/docs/2007#spreadsheet"
/><ns0:id>http://docs.google.com/feeds/documents/private/full/spreadsheet%3Asupercalifragilisticexpeadocious</ns0:id><ns0:link
href="http://foo.com/ccc?key=supercalifragilisticexpeadocious" rel="alternate"
type="text/html" /><ns0:link
href="http://foo.com/feeds/worksheets/supercalifragilisticexpeadocious/private/full"
rel="http://schemas.google.com/spreadsheets/2006#worksheetsfeed"
type="application/atom+xml" /><ns0:link
href="http://docs.google.com/feeds/documents/private/full/spreadsheet%3Asupercalifragilisticexpeadocious"
rel="self" type="application/atom+xml" /><ns0:title type="text">Test Spreadsheet</ns0:title><ns0:updated>2007-07-03T18:03:32.045Z</ns0:updated></ns0:entry><ns0:entry><ns0:content
src="http://docs.google.com/RawDocContents?action=fetch&amp;docID=gr00vy"
type="text/html"
/><ns0:author><ns0:name>test.user</ns0:name><ns0:email>test.user@gmail.com</ns0:email></ns0:author><ns0:category
label="document" scheme="http://schemas.google.com/g/2005#kind"
term="http://schemas.google.com/docs/2007#document"
/><ns0:id>http://docs.google.com/feeds/documents/private/full/document%3Agr00vy</ns0:id><ns0:link
href="http://foobar.com/Doc?id=gr00vy" rel="alternate" type="text/html"
/><ns0:link
href="http://docs.google.com/feeds/documents/private/full/document%3Agr00vy"
rel="self" type="application/atom+xml" /><ns0:title type="text">Test Document</ns0:title><ns0:updated>2007-07-03T18:02:50.338Z</ns0:updated></ns0:entry><ns0:id>http://docs.google.com/feeds/documents/private/full</ns0:id><ns0:link
href="http://docs.google.com" rel="alternate" type="text/html" /><ns0:link
href="http://docs.google.com/feeds/documents/private/full"
rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml"
/><ns0:link href="http://docs.google.com/feeds/documents/private/full"
rel="http://schemas.google.com/g/2005#post" type="application/atom+xml"
/><ns0:link href="http://docs.google.com/feeds/documents/private/full"
rel="self" type="application/atom+xml" /><ns0:title type="text">Available
Documents -
test.user@gmail.com</ns0:title><ns0:updated>2007-07-09T23:07:21.898Z</ns0:updated></ns0:feed>
"""

DOCUMENT_LIST_ENTRY = """<?xml version='1.0' encoding='UTF-8'?>
<ns0:entry xmlns:ns0="http://www.w3.org/2005/Atom"><ns0:content
src="http://foo.com/fm?fmcmd=102&amp;key=supercalifragilisticexpealidocious"
type="text/html"
/><ns0:author><ns0:name>test.user</ns0:name><ns0:email>test.user@gmail.com</ns0:email></ns0:author><ns0:category
label="spreadsheet" scheme="http://schemas.google.com/g/2005#kind"
term="http://schemas.google.com/docs/2007#spreadsheet"
/><ns0:id>http://docs.google.com/feeds/documents/private/full/spreadsheet%3Asupercalifragilisticexpealidocious</ns0:id><ns0:link
href="http://foo.com/ccc?key=supercalifragilisticexpealidocious"
rel="alternate" type="text/html" /><ns0:link
href="http://foo.com/feeds/worksheets/supercalifragilisticexpealidocious/private/full"
rel="http://schemas.google.com/spreadsheets/2006#worksheetsfeed"
type="application/atom+xml" /><ns0:link
href="http://docs.google.com/feeds/documents/private/full/spreadsheet%3Asupercalifragilisticexpealidocious"
rel="self" type="application/atom+xml" /><ns0:title type="text">Test Spreadsheet</ns0:title><ns0:updated>2007-07-03T18:03:32.045Z</ns0:updated></ns0:entry>
"""

BATCH_ENTRY = """<?xml version='1.0' encoding='UTF-8'?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:batch="http://schemas.google.com/gdata/batch" 
       xmlns:g="http://base.google.com/ns/1.0">
  <id>http://www.google.com/base/feeds/items/2173859253842813008</id>
  <published>2006-07-11T14:51:43.560Z</published>
  <updated>2006-07-11T14:51: 43.560Z</updated>
  <title type="text">title</title>
  <content type="html">content</content>
  <link rel="self" 
    type="application/atom+xml" 
    href="http://www.google.com/base/feeds/items/2173859253842813008"/>
  <link rel="edit" 
    type="application/atom+xml" 
    href="http://www.google.com/base/feeds/items/2173859253842813008"/>
  <g:item_type>recipes</g:item_type>
  <batch:operation type="insert"/>
  <batch:id>itemB</batch:id>
  <batch:status code="201" reason="Created"/>
</entry>"""

BATCH_FEED_REQUEST = """<?xml version="1.0" encoding="UTF-8"?>
<feed
  xmlns="http://www.w3.org/2005/Atom"
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:g="http://base.google.com/ns/1.0"
  xmlns:batch="http://schemas.google.com/gdata/batch">
  <title type="text">My Batch Feed</title>
  <entry>
    <id>http://www.google.com/base/feeds/items/13308004346459454600</id>
    <batch:operation type="delete"/>
  </entry>
  <entry>
    <id>http://www.google.com/base/feeds/items/17437536661927313949</id>
    <batch:operation type="delete"/>
  </entry>
  <entry>
    <title type="text">...</title>
    <content type="html">...</content>
    <batch:id>itemA</batch:id>
    <batch:operation type="insert"/>
    <g:item_type>recipes</g:item_type>
  </entry>
  <entry>
    <title type="text">...</title>
    <content type="html">...</content>
    <batch:id>itemB</batch:id>
    <batch:operation type="insert"/>
    <g:item_type>recipes</g:item_type>
  </entry>
</feed>"""

BATCH_FEED_RESULT = """<?xml version="1.0" encoding="UTF-8"?>
<feed
  xmlns="http://www.w3.org/2005/Atom"
  xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
  xmlns:g="http://base.google.com/ns/1.0"
  xmlns:batch="http://schemas.google.com/gdata/batch">
  <id>http://www.google.com/base/feeds/items</id>
  <updated>2006-07-11T14:51:42.894Z</updated>
  <title type="text">My Batch</title>
  <link rel="http://schemas.google.com/g/2005#feed"
    type="application/atom+xml"
    href="http://www.google.com/base/feeds/items"/>
  <link rel="http://schemas.google.com/g/2005#post"
    type="application/atom+xml"
    href="http://www.google.com/base/feeds/items"/>
  <link rel=" http://schemas.google.com/g/2005#batch"
    type="application/atom+xml"
    href="http://www.google.com/base/feeds/items/batch"/>
  <entry>
    <id>http://www.google.com/base/feeds/items/2173859253842813008</id>
    <published>2006-07-11T14:51:43.560Z</published>
    <updated>2006-07-11T14:51: 43.560Z</updated>
    <title type="text">...</title>
    <content type="html">...</content>
    <link rel="self"
      type="application/atom+xml"
      href="http://www.google.com/base/feeds/items/2173859253842813008"/>
    <link rel="edit"
      type="application/atom+xml"
      href="http://www.google.com/base/feeds/items/2173859253842813008"/>
    <g:item_type>recipes</g:item_type>
    <batch:operation type="insert"/>
    <batch:id>itemB</batch:id>
    <batch:status code="201" reason="Created"/>
  </entry>
  <entry>
    <id>http://www.google.com/base/feeds/items/11974645606383737963</id>
    <published>2006-07-11T14:51:43.247Z</published>
    <updated>2006-07-11T14:51: 43.247Z</updated>
    <title type="text">...</title>
    <content type="html">...</content>
    <link rel="self"
      type="application/atom+xml"
      href="http://www.google.com/base/feeds/items/11974645606383737963"/>
    <link rel="edit"
      type="application/atom+xml"
      href="http://www.google.com/base/feeds/items/11974645606383737963"/>
    <g:item_type>recipes</g:item_type>
    <batch:operation type="insert"/>
    <batch:id>itemA</batch:id>
    <batch:status code="201" reason="Created"/>
  </entry>
  <entry>
    <id>http://www.google.com/base/feeds/items/13308004346459454600</id>
    <updated>2006-07-11T14:51:42.894Z</updated>
    <title type="text">Error</title>
    <content type="text">Bad request</content>
    <batch:status code="404"
      reason="Bad request"
      content-type="application/xml">
      <errors>
        <error type="request" reason="Cannot find item"/>
      </errors>
    </batch:status>
  </entry>
  <entry>
    <id>http://www.google.com/base/feeds/items/17437536661927313949</id>
    <updated>2006-07-11T14:51:43.246Z</updated>
    <content type="text">Deleted</content>
    <batch:operation type="delete"/>
    <batch:status code="200" reason="Success"/>
  </entry>
</feed>"""

ALBUM_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/" xmlns:exif="http://schemas.google.com/photos/exif/2007" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#" xmlns:gml="http://www.opengis.net/gml" xmlns:georss="http://www.georss.org/georss" xmlns:photo="http://www.pheed.com/pheed/" xmlns:media="http://search.yahoo.com/mrss/" xmlns:batch="http://schemas.google.com/gdata/batch" xmlns:gphoto="http://schemas.google.com/photos/2007">
  <id>http://picasaweb.google.com/data/feed/api/user/sample.user/albumid/1</id>
  <updated>2007-09-21T18:23:05.000Z</updated>
  <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/photos/2007#album"/>
  <title type="text">Test</title>
  <subtitle type="text"/>
  <rights type="text">public</rights>
  <icon>http://lh6.google.com/sample.user/Rt8WNoDZEJE/AAAAAAAAABk/HQGlDhpIgWo/s160-c/Test.jpg</icon>
  <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml" href="http://picasaweb.google.com/data/feed/api/user/sample.user/albumid/1"/>
  <link rel="alternate" type="text/html" href="http://picasaweb.google.com/sample.user/Test"/>
  <link rel="http://schemas.google.com/photos/2007#slideshow" type="application/x-shockwave-flash" href="http://picasaweb.google.com/s/c/bin/slideshow.swf?host=picasaweb.google.com&amp;RGB=0x000000&amp;feed=http%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2Fsample.user%2Falbumid%2F1%3Falt%3Drss"/>
  <link rel="self" type="application/atom+xml" href="http://picasaweb.google.com/data/feed/api/user/sample.user/albumid/1?start-index=1&amp;max-results=500&amp;kind=photo%2Ctag"/>
  <author>
    <name>sample</name>
    <uri>http://picasaweb.google.com/sample.user</uri>
  </author>
  <generator version="1.00" uri="http://picasaweb.google.com/">Picasaweb</generator>                                                                                                                                     <openSearch:totalResults>4</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>500</openSearch:itemsPerPage>
  <gphoto:id>1</gphoto:id>
  <gphoto:name>Test</gphoto:name>
  <gphoto:location/>
  <gphoto:access>public</gphoto:access>                                                                                                                                                                                  <gphoto:timestamp>1188975600000</gphoto:timestamp>
  <gphoto:numphotos>2</gphoto:numphotos>
  <gphoto:user>sample.user</gphoto:user>
  <gphoto:nickname>sample</gphoto:nickname>
  <gphoto:commentingEnabled>true</gphoto:commentingEnabled>
  <gphoto:commentCount>0</gphoto:commentCount>
  <entry>                                                                                                                                                                                                                  <id>http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/photoid/2</id>
    <published>2007-09-05T20:49:23.000Z</published>
    <updated>2007-09-21T18:23:05.000Z</updated>
    <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/photos/2007#photo"/>
    <title type="text">Aqua Blue.jpg</title>
    <summary type="text">Blue</summary>
    <content type="image/jpeg" src="http://lh4.google.com/sample.user/Rt8WU4DZEKI/AAAAAAAAABY/IVgLqmnzJII/Aqua%20Blue.jpg"/>                                                                                               <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml" href="http://picasaweb.google.com/data/feed/api/user/sample.user/albumid/1/photoid/2"/>
    <link rel="alternate" type="text/html" href="http://picasaweb.google.com/sample.user/Test/photo#2"/>
    <link rel="self" type="application/atom+xml" href="http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/photoid/2"/>
    <gphoto:id>2</gphoto:id>
    <gphoto:version>1190398985145172</gphoto:version>
    <gphoto:position>0.0</gphoto:position>
    <gphoto:albumid>1</gphoto:albumid>                                                                                                                                                                                     <gphoto:width>2560</gphoto:width>
    <gphoto:height>1600</gphoto:height>
    <gphoto:size>883405</gphoto:size>
    <gphoto:client/>
    <gphoto:checksum/>
    <gphoto:timestamp>1189025362000</gphoto:timestamp>
    <exif:tags>                                                                                                                                                                                                              <exif:flash>true</exif:flash>
      <exif:imageUniqueID>c041ce17aaa637eb656c81d9cf526c24</exif:imageUniqueID>
    </exif:tags>
    <gphoto:commentingEnabled>true</gphoto:commentingEnabled>
    <gphoto:commentCount>1</gphoto:commentCount>
    <media:group>
      <media:title type="plain">Aqua Blue.jpg</media:title>                                                                                                                                                                  <media:description type="plain">Blue</media:description>
      <media:keywords>tag, test</media:keywords>
      <media:content url="http://lh4.google.com/sample.user/Rt8WU4DZEKI/AAAAAAAAABY/IVgLqmnzJII/Aqua%20Blue.jpg" height="1600" width="2560" type="image/jpeg" medium="image"/>
      <media:thumbnail url="http://lh4.google.com/sample.user/Rt8WU4DZEKI/AAAAAAAAABY/IVgLqmnzJII/s72/Aqua%20Blue.jpg" height="45" width="72"/>
      <media:thumbnail url="http://lh4.google.com/sample.user/Rt8WU4DZEKI/AAAAAAAAABY/IVgLqmnzJII/s144/Aqua%20Blue.jpg" height="90" width="144"/>
      <media:thumbnail url="http://lh4.google.com/sample.user/Rt8WU4DZEKI/AAAAAAAAABY/IVgLqmnzJII/s288/Aqua%20Blue.jpg" height="180" width="288"/>
      <media:credit>sample</media:credit>
    </media:group>
  </entry>
  <entry>
    <id>http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/photoid/3</id>
    <published>2007-09-05T20:49:24.000Z</published>
    <updated>2007-09-21T18:19:38.000Z</updated>
    <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/photos/2007#photo"/>
    <title type="text">Aqua Graphite.jpg</title>
    <summary type="text">Gray</summary>
    <content type="image/jpeg" src="http://lh5.google.com/sample.user/Rt8WVIDZELI/AAAAAAAAABg/d7e0i7gvhNU/Aqua%20Graphite.jpg"/>
    <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml" href="http://picasaweb.google.com/data/feed/api/user/sample.user/albumid/1/photoid/3"/>
    <link rel="alternate" type="text/html" href="http://picasaweb.google.com/sample.user/Test/photo#3"/>
    <link rel="self" type="application/atom+xml" href="http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/photoid/3"/>
    <gphoto:id>3</gphoto:id>
    <gphoto:version>1190398778006402</gphoto:version>
    <gphoto:position>1.0</gphoto:position>
    <gphoto:albumid>1</gphoto:albumid>
    <gphoto:width>2560</gphoto:width>
    <gphoto:height>1600</gphoto:height>
    <gphoto:size>798334</gphoto:size>
    <gphoto:client/>
    <gphoto:checksum/>
    <gphoto:timestamp>1189025363000</gphoto:timestamp>
    <exif:tags>
      <exif:flash>true</exif:flash>
      <exif:imageUniqueID>a5ce2e36b9df7d3cb081511c72e73926</exif:imageUniqueID>
    </exif:tags>
    <gphoto:commentingEnabled>true</gphoto:commentingEnabled>
    <gphoto:commentCount>0</gphoto:commentCount>
    <media:group>
      <media:title type="plain">Aqua Graphite.jpg</media:title>
      <media:description type="plain">Gray</media:description>
      <media:keywords/>
      <media:content url="http://lh5.google.com/sample.user/Rt8WVIDZELI/AAAAAAAAABg/d7e0i7gvhNU/Aqua%20Graphite.jpg" height="1600" width="2560" type="image/jpeg" medium="image"/>
      <media:thumbnail url="http://lh5.google.com/sample.user/Rt8WVIDZELI/AAAAAAAAABg/d7e0i7gvhNU/s72/Aqua%20Graphite.jpg" height="45" width="72"/>
      <media:thumbnail url="http://lh5.google.com/sample.user/Rt8WVIDZELI/AAAAAAAAABg/d7e0i7gvhNU/s144/Aqua%20Graphite.jpg" height="90" width="144"/>
      <media:thumbnail url="http://lh5.google.com/sample.user/Rt8WVIDZELI/AAAAAAAAABg/d7e0i7gvhNU/s288/Aqua%20Graphite.jpg" height="180" width="288"/>
      <media:credit>sample</media:credit>
    </media:group>
  </entry>
  <entry>
    <id>http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/tag/tag</id>
    <updated>2007-09-05T20:49:24.000Z</updated>
    <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/photos/2007#tag"/>
    <title type="text">tag</title>
    <summary type="text">tag</summary>
    <link rel="alternate" type="text/html" href="http://picasaweb.google.com/lh/searchbrowse?q=tag&amp;psc=G&amp;uname=sample.user&amp;filter=0"/>
    <link rel="self" type="application/atom+xml" href="http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/tag/tag"/>
    <author>
      <name>sample</name>
      <uri>http://picasaweb.google.com/sample.user</uri>
    </author>
  </entry>
  <entry>
    <id>http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/tag/test</id>
    <updated>2007-09-05T20:49:24.000Z</updated>
    <category scheme="http://schemas.google.com/g/2005#kind" term="http://schemas.google.com/photos/2007#tag"/>
    <title type="text">test</title>
    <summary type="text">test</summary>
    <link rel="alternate" type="text/html" href="http://picasaweb.google.com/lh/searchbrowse?q=test&amp;psc=G&amp;uname=sample.user&amp;filter=0"/>
    <link rel="self" type="application/atom+xml" href="http://picasaweb.google.com/data/entry/api/user/sample.user/albumid/1/tag/test"/>
    <author>
      <name>sample</name>
      <uri>http://picasaweb.google.com/sample.user</uri>
    </author>
  </entry>
</feed>"""

CODE_SEARCH_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:opensearch="http://a9.com/-/spec/opensearchrss/1.0/" xmlns:gcs="http://schemas.google.com/codesearch/2006" xml:base="http://www.google.com">
<id>http://www.google.com/codesearch/feeds/search?q=malloc</id>
<updated>2007-12-19T16:08:04Z</updated> 
<title type="text">Google Code Search</title>
<generator version="1.0" uri="http://www.google.com/codesearch">Google Code Search</generator>
<opensearch:totalResults>2530000</opensearch:totalResults>
<opensearch:startIndex>1</opensearch:startIndex>
<author>
<name>Google Code Search</name>

<uri>http://www.google.com/codesearch</uri>
</author>
<link rel="http://schemas.google.com/g/2006#feed" type="application/atom+xml" href="http://schemas.google.com/codesearch/2006"/>
<link rel="self" type="application/atom+xml" href="http://www.google.com/codesearch/feeds/search?q=malloc"/>
<link rel="next" type="application/atom+xml"  href="http://www.google.com/codesearch/feeds/search?q=malloc&amp;start-index=11"/>
<link rel="alternate" type="text/html" href="http://www.google.com/codesearch?q=malloc"/>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:LDjwp-Iqc7U:84hEYaYsZk8:xDGReDhvNi0&amp;sa=N&amp;ct=rx&amp;cd=1&amp;cs_p=http://www.gnu.org&amp;cs_f=software/autoconf/manual/autoconf-2.60/autoconf.html-002&amp;cs_p=http://www.gnu.org&amp;cs_f=software/autoconf/manual/autoconf-2.60/autoconf.html-002#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">software/autoconf/manual/autoconf-2.60/autoconf.html</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:LDjwp-Iqc7U:84hEYaYsZk8:xDGReDhvNi0&amp;sa=N&amp;ct=rx&amp;cd=1&amp;cs_p=http://www.gnu.org&amp;cs_f=software/autoconf/manual/autoconf-2.60/autoconf.html-002&amp;cs_p=http://www.gnu.org&amp;cs_f=software/autoconf/manual/autoconf-2.60/autoconf.html-002#first"/><gcs:package name="http://www.gnu.org" uri="http://www.gnu.org"></gcs:package><gcs:file name="software/autoconf/manual/autoconf-2.60/autoconf.html-002"></gcs:file><content type="text/html">&lt;pre&gt;     8:      void *&lt;b&gt;malloc&lt;/b&gt; ();
        

&lt;/pre&gt;</content><gcs:match lineNumber="4" type="text/html">&lt;pre&gt;     #undef &lt;b&gt;malloc&lt;/b&gt;
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="8" type="text/html">&lt;pre&gt;     void *&lt;b&gt;malloc&lt;/b&gt; ();

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="14" type="text/html">&lt;pre&gt;     rpl_&lt;b&gt;malloc&lt;/b&gt; (size_t n)
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="18" type="text/html">&lt;pre&gt;       return &lt;b&gt;malloc&lt;/b&gt; (n);

&lt;/pre&gt;</gcs:match></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:h4hfh-fV-jI:niBq_bwWZNs:H0OhClf0HWQ&amp;sa=N&amp;ct=rx&amp;cd=2&amp;cs_p=ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz&amp;cs_f=guile-1.6.8/libguile/mallocs.c&amp;cs_p=ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz&amp;cs_f=guile-1.6.8/libguile/mallocs.c#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">guile-1.6.8/libguile/mallocs.c</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:h4hfh-fV-jI:niBq_bwWZNs:H0OhClf0HWQ&amp;sa=N&amp;ct=rx&amp;cd=2&amp;cs_p=ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz&amp;cs_f=guile-1.6.8/libguile/mallocs.c&amp;cs_p=ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz&amp;cs_f=guile-1.6.8/libguile/mallocs.c#first"/><gcs:package name="ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz" uri="ftp://ftp.gnu.org/gnu/guile/guile-1.6.8.tar.gz"></gcs:package><gcs:file name="guile-1.6.8/libguile/mallocs.c"></gcs:file><content type="text/html">&lt;pre&gt;    86: {
          scm_t_bits mem = n ? (scm_t_bits) &lt;b&gt;malloc&lt;/b&gt; (n) : 0;
          if (n &amp;amp;&amp;amp; !mem)

&lt;/pre&gt;</content><gcs:match lineNumber="54" type="text/html">&lt;pre&gt;#include &amp;lt;&lt;b&gt;malloc&lt;/b&gt;.h&amp;gt;
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="62" type="text/html">&lt;pre&gt;scm_t_bits scm_tc16_&lt;b&gt;malloc&lt;/b&gt;;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="66" type="text/html">&lt;pre&gt;&lt;b&gt;malloc&lt;/b&gt;_free (SCM ptr)
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="75" type="text/html">&lt;pre&gt;&lt;b&gt;malloc&lt;/b&gt;_print (SCM exp, SCM port, scm_print_state *pstate SCM_UNUSED)

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="77" type="text/html">&lt;pre&gt;  scm_puts(&amp;quot;#&amp;lt;&lt;b&gt;malloc&lt;/b&gt; &amp;quot;, port);
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="87" type="text/html">&lt;pre&gt;  scm_t_bits mem = n ? (scm_t_bits) &lt;b&gt;malloc&lt;/b&gt; (n) : 0;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="90" type="text/html">&lt;pre&gt;  SCM_RETURN_NEWSMOB (scm_tc16_&lt;b&gt;malloc&lt;/b&gt;, mem);
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="98" type="text/html">&lt;pre&gt;  scm_tc16_&lt;b&gt;malloc&lt;/b&gt; = scm_make_smob_type (&amp;quot;&lt;b&gt;malloc&lt;/b&gt;&amp;quot;, 0);

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="99" type="text/html">&lt;pre&gt;  scm_set_smob_free (scm_tc16_&lt;b&gt;malloc&lt;/b&gt;, &lt;b&gt;malloc&lt;/b&gt;_free);
&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>

<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:9wyZUG-N_30:7_dFxoC1ZrY:C0_iYbFj90M&amp;sa=N&amp;ct=rx&amp;cd=3&amp;cs_p=http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz&amp;cs_f=bash-3.0/lib/malloc/alloca.c&amp;cs_p=http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz&amp;cs_f=bash-3.0/lib/malloc/alloca.c#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">bash-3.0/lib/malloc/alloca.c</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:9wyZUG-N_30:7_dFxoC1ZrY:C0_iYbFj90M&amp;sa=N&amp;ct=rx&amp;cd=3&amp;cs_p=http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz&amp;cs_f=bash-3.0/lib/malloc/alloca.c&amp;cs_p=http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz&amp;cs_f=bash-3.0/lib/malloc/alloca.c#first"/><gcs:package name="http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz" uri="http://ftp.gnu.org/gnu/bash/bash-3.0.tar.gz"></gcs:package><gcs:file name="bash-3.0/lib/malloc/alloca.c"></gcs:file><content type="text/html">&lt;pre&gt;    78: #ifndef emacs
        #define &lt;b&gt;malloc&lt;/b&gt; x&lt;b&gt;malloc&lt;/b&gt;
        extern pointer x&lt;b&gt;malloc&lt;/b&gt; ();

&lt;/pre&gt;</content><gcs:match lineNumber="69" type="text/html">&lt;pre&gt;   &lt;b&gt;malloc&lt;/b&gt;.  The Emacs executable needs alloca to call x&lt;b&gt;malloc&lt;/b&gt;, because
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="70" type="text/html">&lt;pre&gt;   ordinary &lt;b&gt;malloc&lt;/b&gt; isn&amp;#39;t protected from input signals.  On the other

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="71" type="text/html">&lt;pre&gt;   hand, the utilities in lib-src need alloca to call &lt;b&gt;malloc&lt;/b&gt;; some of
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="72" type="text/html">&lt;pre&gt;   them are very simple, and don&amp;#39;t have an x&lt;b&gt;malloc&lt;/b&gt; routine.

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="76" type="text/html">&lt;pre&gt;   Callers below should use &lt;b&gt;malloc&lt;/b&gt;.  */
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="79" type="text/html">&lt;pre&gt;#define &lt;b&gt;malloc&lt;/b&gt; x&lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="80" type="text/html">&lt;pre&gt;extern pointer x&lt;b&gt;malloc&lt;/b&gt; ();
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="132" type="text/html">&lt;pre&gt;   It is very important that sizeof(header) agree with &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="198" type="text/html">&lt;pre&gt;    register pointer new = &lt;b&gt;malloc&lt;/b&gt; (sizeof (header) + size);
&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:uhVCKyPcT6k:8juMxxzmUJw:H7_IDsTB2L4&amp;sa=N&amp;ct=rx&amp;cd=4&amp;cs_p=http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2&amp;cs_f=mozilla/xpcom/build/malloc.c&amp;cs_p=http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2&amp;cs_f=mozilla/xpcom/build/malloc.c#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">mozilla/xpcom/build/malloc.c</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:uhVCKyPcT6k:8juMxxzmUJw:H7_IDsTB2L4&amp;sa=N&amp;ct=rx&amp;cd=4&amp;cs_p=http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2&amp;cs_f=mozilla/xpcom/build/malloc.c&amp;cs_p=http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2&amp;cs_f=mozilla/xpcom/build/malloc.c#first"/><gcs:package name="http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2" uri="http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla1.7b/src/mozilla-source-1.7b-source.tar.bz2"></gcs:package><gcs:file name="mozilla/xpcom/build/malloc.c"></gcs:file><content type="text/html">&lt;pre&gt;    54:      http://gee.cs.oswego.edu/dl/html/&lt;b&gt;malloc&lt;/b&gt;.html
        
          You may already by default be using a c library containing a &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</content><gcs:match lineNumber="4" type="text/html">&lt;pre&gt;/* ---------- To make a &lt;b&gt;malloc&lt;/b&gt;.h, start cutting here ------------ */
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="22" type="text/html">&lt;pre&gt;   Note: There may be an updated version of this &lt;b&gt;malloc&lt;/b&gt; obtainable at

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="23" type="text/html">&lt;pre&gt;           ftp://gee.cs.oswego.edu/pub/misc/&lt;b&gt;malloc&lt;/b&gt;.c
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="34" type="text/html">&lt;pre&gt;* Why use this &lt;b&gt;malloc&lt;/b&gt;?

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="37" type="text/html">&lt;pre&gt;  most tunable &lt;b&gt;malloc&lt;/b&gt; ever written. However it is among the fastest
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="40" type="text/html">&lt;pre&gt;  allocator for &lt;b&gt;malloc&lt;/b&gt;-intensive programs.

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="54" type="text/html">&lt;pre&gt;     http://gee.cs.oswego.edu/dl/html/&lt;b&gt;malloc&lt;/b&gt;.html
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="56" type="text/html">&lt;pre&gt;  You may already by default be using a c library containing a &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="57" type="text/html">&lt;pre&gt;  that is somehow based on some version of this &lt;b&gt;malloc&lt;/b&gt; (for example in
&lt;/pre&gt;</gcs:match><rights>Mozilla</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:4n1P2HVOISs:Ybbpph0wR2M:OhIN_sDrG0U&amp;sa=N&amp;ct=rx&amp;cd=5&amp;cs_p=http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz&amp;cs_f=hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh&amp;cs_p=http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz&amp;cs_f=hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:4n1P2HVOISs:Ybbpph0wR2M:OhIN_sDrG0U&amp;sa=N&amp;ct=rx&amp;cd=5&amp;cs_p=http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz&amp;cs_f=hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh&amp;cs_p=http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz&amp;cs_f=hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh#first"/><gcs:package name="http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz" uri="http://regexps.srparish.net/src/hackerlab/hackerlab-1.0pre2.tar.gz"></gcs:package><gcs:file name="hackerlab-1.0pre2/src/hackerlab/tests/mem-tests/unit-must-malloc.sh"></gcs:file><content type="text/html">&lt;pre&gt;    11: echo ================ unit-must-&lt;b&gt;malloc&lt;/b&gt; tests ================
        ./unit-must-&lt;b&gt;malloc&lt;/b&gt;
        echo ...passed

&lt;/pre&gt;</content><gcs:match lineNumber="2" type="text/html">&lt;pre&gt;# tag: Tom Lord Tue Dec  4 14:54:29 2001 (mem-tests/unit-must-&lt;b&gt;malloc&lt;/b&gt;.sh)
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="11" type="text/html">&lt;pre&gt;echo ================ unit-must-&lt;b&gt;malloc&lt;/b&gt; tests ================

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="12" type="text/html">&lt;pre&gt;./unit-must-&lt;b&gt;malloc&lt;/b&gt;
&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:GzkwiWG266M:ykuz3bG00ws:2sTvVSif08g&amp;sa=N&amp;ct=rx&amp;cd=6&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2&amp;cs_f=tar-1.14/lib/malloc.c&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2&amp;cs_f=tar-1.14/lib/malloc.c#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">tar-1.14/lib/malloc.c</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:GzkwiWG266M:ykuz3bG00ws:2sTvVSif08g&amp;sa=N&amp;ct=rx&amp;cd=6&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2&amp;cs_f=tar-1.14/lib/malloc.c&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2&amp;cs_f=tar-1.14/lib/malloc.c#first"/><gcs:package name="http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2" uri="http://ftp.gnu.org/gnu/tar/tar-1.14.tar.bz2"></gcs:package><gcs:file name="tar-1.14/lib/malloc.c"></gcs:file><content type="text/html">&lt;pre&gt;    22: #endif
        #undef &lt;b&gt;malloc&lt;/b&gt;
        

&lt;/pre&gt;</content><gcs:match lineNumber="1" type="text/html">&lt;pre&gt;/* Work around bug on some systems where &lt;b&gt;malloc&lt;/b&gt; (0) fails.
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="23" type="text/html">&lt;pre&gt;#undef &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="31" type="text/html">&lt;pre&gt;rpl_&lt;b&gt;malloc&lt;/b&gt; (size_t n)
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="35" type="text/html">&lt;pre&gt;  return &lt;b&gt;malloc&lt;/b&gt; (n);

&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:o_TFIeBY6dY:ktI_dt8wPao:AI03BD1Dz0Y&amp;sa=N&amp;ct=rx&amp;cd=7&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz&amp;cs_f=tar-1.16.1/lib/malloc.c&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz&amp;cs_f=tar-1.16.1/lib/malloc.c#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">tar-1.16.1/lib/malloc.c</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:o_TFIeBY6dY:ktI_dt8wPao:AI03BD1Dz0Y&amp;sa=N&amp;ct=rx&amp;cd=7&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz&amp;cs_f=tar-1.16.1/lib/malloc.c&amp;cs_p=http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz&amp;cs_f=tar-1.16.1/lib/malloc.c#first"/><gcs:package name="http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz" uri="http://ftp.gnu.org/gnu/tar/tar-1.16.1.tar.gz"></gcs:package><gcs:file name="tar-1.16.1/lib/malloc.c"></gcs:file><content type="text/html">&lt;pre&gt;    21: #include &amp;lt;config.h&amp;gt;
        #undef &lt;b&gt;malloc&lt;/b&gt;
        

&lt;/pre&gt;</content><gcs:match lineNumber="1" type="text/html">&lt;pre&gt;/* &lt;b&gt;malloc&lt;/b&gt;() function that is glibc compatible.
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="22" type="text/html">&lt;pre&gt;#undef &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="30" type="text/html">&lt;pre&gt;rpl_&lt;b&gt;malloc&lt;/b&gt; (size_t n)
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="34" type="text/html">&lt;pre&gt;  return &lt;b&gt;malloc&lt;/b&gt; (n);

&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:_ibw-VLkMoI:jBOtIJSmFd4:-0NUEVeCwfY&amp;sa=N&amp;ct=rx&amp;cd=8&amp;cs_p=http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2&amp;cs_f=uClibc-0.9.29/include/malloc.h&amp;cs_p=http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2&amp;cs_f=uClibc-0.9.29/include/malloc.h#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">uClibc-0.9.29/include/malloc.h</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:_ibw-VLkMoI:jBOtIJSmFd4:-0NUEVeCwfY&amp;sa=N&amp;ct=rx&amp;cd=8&amp;cs_p=http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2&amp;cs_f=uClibc-0.9.29/include/malloc.h&amp;cs_p=http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2&amp;cs_f=uClibc-0.9.29/include/malloc.h#first"/><gcs:package name="http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2" uri="http://freshmeat.net/redir/uclibc/20616/url_bz2/uClibc-0.9.28.1.tar.bz2"></gcs:package><gcs:file name="uClibc-0.9.29/include/malloc.h"></gcs:file><content type="text/html">&lt;pre&gt;     1: /* Prototypes and definition for &lt;b&gt;malloc&lt;/b&gt; implementation.
           Copyright (C) 1996, 1997, 1999, 2000 Free Software Foundation, Inc.

&lt;/pre&gt;</content><gcs:match lineNumber="1" type="text/html">&lt;pre&gt;/* Prototypes and definition for &lt;b&gt;malloc&lt;/b&gt; implementation.
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="26" type="text/html">&lt;pre&gt;  `pt&lt;b&gt;malloc&lt;/b&gt;&amp;#39;, a &lt;b&gt;malloc&lt;/b&gt; implementation for multiple threads without

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="28" type="text/html">&lt;pre&gt;  See the files `pt&lt;b&gt;malloc&lt;/b&gt;.c&amp;#39; or `COPYRIGHT&amp;#39; for copying conditions.
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="32" type="text/html">&lt;pre&gt;  This work is mainly derived from &lt;b&gt;malloc&lt;/b&gt;-2.6.4 by Doug Lea

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="35" type="text/html">&lt;pre&gt;                 ftp://g.oswego.edu/pub/misc/&lt;b&gt;malloc&lt;/b&gt;.c
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="40" type="text/html">&lt;pre&gt;  `pt&lt;b&gt;malloc&lt;/b&gt;.c&amp;#39;.

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="45" type="text/html">&lt;pre&gt;# define __&lt;b&gt;malloc&lt;/b&gt;_ptr_t  void *
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="51" type="text/html">&lt;pre&gt;# define __&lt;b&gt;malloc&lt;/b&gt;_ptr_t  char *

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="56" type="text/html">&lt;pre&gt;# define __&lt;b&gt;malloc&lt;/b&gt;_size_t size_t
&lt;/pre&gt;</gcs:match><rights>LGPL</rights></entry>
<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:F6qHcZ9vefo:bTX7o9gKfks:hECF4r_eKC0&amp;sa=N&amp;ct=rx&amp;cd=9&amp;cs_p=http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz&amp;cs_f=glibc-2.0.1/hurd/hurdmalloc.h&amp;cs_p=http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz&amp;cs_f=glibc-2.0.1/hurd/hurdmalloc.h#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">glibc-2.0.1/hurd/hurdmalloc.h</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:F6qHcZ9vefo:bTX7o9gKfks:hECF4r_eKC0&amp;sa=N&amp;ct=rx&amp;cd=9&amp;cs_p=http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz&amp;cs_f=glibc-2.0.1/hurd/hurdmalloc.h&amp;cs_p=http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz&amp;cs_f=glibc-2.0.1/hurd/hurdmalloc.h#first"/><gcs:package name="http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz" uri="http://ftp.gnu.org/gnu/glibc/glibc-2.0.1.tar.gz"></gcs:package><gcs:file name="glibc-2.0.1/hurd/hurdmalloc.h"></gcs:file><content type="text/html">&lt;pre&gt;    15: #define &lt;b&gt;malloc&lt;/b&gt;   _hurd_&lt;b&gt;malloc&lt;/b&gt;
        #define realloc _hurd_realloc

&lt;/pre&gt;</content><gcs:match lineNumber="3" type="text/html">&lt;pre&gt;   All hurd-internal code which uses &lt;b&gt;malloc&lt;/b&gt; et al includes this file so it
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="4" type="text/html">&lt;pre&gt;   will use the internal &lt;b&gt;malloc&lt;/b&gt; routines _hurd_{&lt;b&gt;malloc&lt;/b&gt;,realloc,free}

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="7" type="text/html">&lt;pre&gt;   of &lt;b&gt;malloc&lt;/b&gt; et al is the unixoid one using sbrk.
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="11" type="text/html">&lt;pre&gt;extern void *_hurd_&lt;b&gt;malloc&lt;/b&gt; (size_t);

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="15" type="text/html">&lt;pre&gt;#define &lt;b&gt;malloc&lt;/b&gt;        _hurd_&lt;b&gt;malloc&lt;/b&gt;
&lt;/pre&gt;</gcs:match><rights>GPL</rights></entry>

<entry><id>http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:CHUvHYzyLc8:pdcAfzDA6lY:wjofHuNLTHg&amp;sa=N&amp;ct=rx&amp;cd=10&amp;cs_p=ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2&amp;cs_f=httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h&amp;cs_p=ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2&amp;cs_f=httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h#first</id><updated>2007-12-19T16:08:04Z</updated><author><name>Code owned by external author.</name></author><title type="text">httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h</title><link rel="alternate" type="text/html" href="http://www.google.com/codesearch?hl=en&amp;q=+malloc+show:CHUvHYzyLc8:pdcAfzDA6lY:wjofHuNLTHg&amp;sa=N&amp;ct=rx&amp;cd=10&amp;cs_p=ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2&amp;cs_f=httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h&amp;cs_p=ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2&amp;cs_f=httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h#first"/><gcs:package name="ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2" uri="ftp://apache.mirrors.pair.com/httpd/httpd-2.2.4.tar.bz2"></gcs:package><gcs:file name="httpd-2.2.4/srclib/apr/include/arch/netware/apr_private.h"></gcs:file><content type="text/html">&lt;pre&gt;   173: #undef &lt;b&gt;malloc&lt;/b&gt;
        #define &lt;b&gt;malloc&lt;/b&gt;(x) library_&lt;b&gt;malloc&lt;/b&gt;(gLibHandle,x)

&lt;/pre&gt;</content><gcs:match lineNumber="170" type="text/html">&lt;pre&gt;/* Redefine &lt;b&gt;malloc&lt;/b&gt; to use the library &lt;b&gt;malloc&lt;/b&gt; call so
&lt;/pre&gt;</gcs:match><gcs:match lineNumber="173" type="text/html">&lt;pre&gt;#undef &lt;b&gt;malloc&lt;/b&gt;

&lt;/pre&gt;</gcs:match><gcs:match lineNumber="174" type="text/html">&lt;pre&gt;#define &lt;b&gt;malloc&lt;/b&gt;(x) library_&lt;b&gt;malloc&lt;/b&gt;(gLibHandle,x)
&lt;/pre&gt;</gcs:match><rights>Apache</rights></entry>

</feed>"""

YOUTUBE_VIDEO_FEED = """<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gml='http://www.opengis.net/gml' xmlns:georss='http://www.georss.org/georss' xmlns:media='http://search.yahoo.com/mrss/' xmlns:yt='http://gdata.youtube.com/schemas/2007' xmlns:gd='http://schemas.google.com/g/2005'><id>http://gdata.youtube.com/feeds/api/standardfeeds/top_rated</id><updated>2008-05-14T02:24:07.000-07:00</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#video'/><title type='text'>Top Rated</title><logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo><link rel='alternate' type='text/html' href='http://www.youtube.com/browse?s=tr'/><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?start-index=1&amp;max-results=25'/><link rel='next' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?start-index=26&amp;max-results=25'/><author><name>YouTube</name><uri>http://www.youtube.com/</uri></author><generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator><openSearch:totalResults>100</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage>
<entry><id>http://gdata.youtube.com/feeds/api/videos/C71ypXYGho8</id><published>2008-03-20T10:17:27.000-07:00</published><updated>2008-05-14T04:26:37.000-07:00</updated><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='karyn'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='garcia'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='me'/><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#video'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='boyfriend'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='por'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='te'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='odeio'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='amar'/><category scheme='http://gdata.youtube.com/schemas/2007/categories.cat' term='Music' label='Music'/><title type='text'>Me odeio por te amar - KARYN GARCIA</title><content type='text'>http://www.karyngarcia.com.br</content><link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=C71ypXYGho8'/><link rel='http://gdata.youtube.com/schemas/2007#video.related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/C71ypXYGho8/related'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/standardfeeds/top_rated/C71ypXYGho8'/><author><name>TvKarynGarcia</name><uri>http://gdata.youtube.com/feeds/api/users/tvkaryngarcia</uri></author><media:group><media:title type='plain'>Me odeio por te amar - KARYN GARCIA</media:title><media:description type='plain'>http://www.karyngarcia.com.br</media:description><media:keywords>amar, boyfriend, garcia, karyn, me, odeio, por, te</media:keywords><yt:duration seconds='203'/><media:category label='Music' scheme='http://gdata.youtube.com/schemas/2007/categories.cat'>Music</media:category><media:category label='test111' scheme='http://gdata.youtube.com/schemas/2007/developertags.cat'>test111</media:category><media:category label='test222' scheme='http://gdata.youtube.com/schemas/2007/developertags.cat'>test222</media:category><media:content url='http://www.youtube.com/v/C71ypXYGho8' type='application/x-shockwave-flash' medium='video' isDefault='true' expression='full' duration='203' yt:format='5'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQmPhgZ2pXK9CxMYDSANFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='203' yt:format='1'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQmPhgZ2pXK9CxMYESARFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='203' yt:format='6'/><media:player url='http://www.youtube.com/watch?v=C71ypXYGho8'/><media:thumbnail url='http://img.youtube.com/vi/C71ypXYGho8/2.jpg' height='97' width='130' time='00:01:41.500'/><media:thumbnail url='http://img.youtube.com/vi/C71ypXYGho8/1.jpg' height='97' width='130' time='00:00:50.750'/><media:thumbnail url='http://img.youtube.com/vi/C71ypXYGho8/3.jpg' height='97' width='130' time='00:02:32.250'/><media:thumbnail url='http://img.youtube.com/vi/C71ypXYGho8/0.jpg' height='240' width='320' time='00:01:41.500'/></media:group><yt:statistics viewCount='138864' favoriteCount='2474'/><gd:rating min='1' max='5' numRaters='4626' average='4.95'/><gd:comments><gd:feedLink href='http://gdata.youtube.com/feeds/api/videos/C71ypXYGho8/comments' countHint='27'/></gd:comments></entry>
<entry><id>http://gdata.youtube.com/feeds/api/videos/gsVaTyb1tBw</id><published>2008-02-15T04:31:45.000-08:00</published><updated>2008-05-14T05:09:42.000-07:00</updated><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='extreme'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='cam'/><category scheme='http://gdata.youtube.com/schemas/2007/categories.cat' term='Sports' label='Sports'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='alcala'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='kani'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='helmet'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='campillo'/><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#video'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='pato'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='dirt'/><title type='text'>extreme helmet cam Kani, Keil and Pato</title><content type='text'>trimmed</content><link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=gsVaTyb1tBw'/><link rel='http://gdata.youtube.com/schemas/2007#video.responses' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/gsVaTyb1tBw/responses'/><link rel='http://gdata.youtube.com/schemas/2007#video.related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/gsVaTyb1tBw/related'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/standardfeeds/recently_featured/gsVaTyb1tBw'/><author><name>peraltamagic</name><uri>http://gdata.youtube.com/feeds/api/users/peraltamagic</uri></author><media:group><media:title type='plain'>extreme helmet cam Kani, Keil and Pato</media:title><media:description type='plain'>trimmed</media:description><media:keywords>alcala, cam, campillo, dirt, extreme, helmet, kani, pato</media:keywords><yt:duration seconds='31'/><media:category label='Sports' scheme='http://gdata.youtube.com/schemas/2007/categories.cat'>Sports</media:category><media:content url='http://www.youtube.com/v/gsVaTyb1tBw' type='application/x-shockwave-flash' medium='video' isDefault='true' expression='full' duration='31' yt:format='5'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQkctPUmT1rFghMYDSANFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='31' yt:format='1'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQkctPUmT1rFghMYESARFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='31' yt:format='6'/><media:player url='http://www.youtube.com/watch?v=gsVaTyb1tBw'/><media:thumbnail url='http://img.youtube.com/vi/gsVaTyb1tBw/2.jpg' height='97' width='130' time='00:00:15.500'/><media:thumbnail url='http://img.youtube.com/vi/gsVaTyb1tBw/1.jpg' height='97' width='130' time='00:00:07.750'/><media:thumbnail url='http://img.youtube.com/vi/gsVaTyb1tBw/3.jpg' height='97' width='130' time='00:00:23.250'/><media:thumbnail url='http://img.youtube.com/vi/gsVaTyb1tBw/0.jpg' height='240' width='320' time='00:00:15.500'/></media:group><yt:statistics viewCount='489941' favoriteCount='561'/><gd:rating min='1' max='5' numRaters='1255' average='4.11'/><gd:comments><gd:feedLink href='http://gdata.youtube.com/feeds/api/videos/gsVaTyb1tBw/comments' countHint='1116'/></gd:comments></entry>
</feed>"""

YOUTUBE_ENTRY_PRIVATE = """<?xml version='1.0' encoding='utf-8'?>
<entry xmlns='http://www.w3.org/2005/Atom' 
xmlns:media='http://search.yahoo.com/mrss/' 
xmlns:gd='http://schemas.google.com/g/2005' 
xmlns:yt='http://gdata.youtube.com/schemas/2007' 
xmlns:gml='http://www.opengis.net/gml' 
xmlns:georss='http://www.georss.org/georss'
xmlns:app='http://purl.org/atom/app#'>
  <id>http://gdata.youtube.com/feeds/videos/UMFI1hdm96E</id>
  <published>2007-01-07T01:50:15.000Z</published>
  <updated>2007-01-07T01:50:15.000Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind'
  term='http://gdata.youtube.com/schemas/2007#video' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='barkley' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='singing' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='acoustic' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='cover' />
  <category scheme='http://gdata.youtube.com/schemas/2007/categories.cat'
  term='Music' label='Music' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='gnarls' />
  <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat'
  term='music' />
  <title type='text'>"Crazy (Gnarles Barkley)" - Acoustic Cover</title>
  <content type='html'>&lt;div style="color: #000000;font-family:
  Arial, Helvetica, sans-serif; font-size:12px; font-size: 12px;
  width: 555px;"&gt;&lt;table cellspacing="0" cellpadding="0"
  border="0"&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td width="140"
  valign="top" rowspan="2"&gt;&lt;div style="border: 1px solid
  #999999; margin: 0px 10px 5px 0px;"&gt;&lt;a
  href="http://www.youtube.com/watch?v=UMFI1hdm96E"&gt;&lt;img
  alt=""
  src="http://img.youtube.com/vi/UMFI1hdm96E/2.jpg"&gt;&lt;/a&gt;&lt;/div&gt;&lt;/td&gt;
  &lt;td width="256" valign="top"&gt;&lt;div style="font-size:
  12px; font-weight: bold;"&gt;&lt;a style="font-size: 15px;
  font-weight: bold; font-decoration: none;"
  href="http://www.youtube.com/watch?v=UMFI1hdm96E"&gt;&amp;quot;Crazy
  (Gnarles Barkley)&amp;quot; - Acoustic Cover&lt;/a&gt;
  &lt;br&gt;&lt;/div&gt; &lt;div style="font-size: 12px; margin:
  3px 0px;"&gt;&lt;span&gt;Gnarles Barkley acoustic cover
  http://www.myspace.com/davidchoimusic&lt;/span&gt;&lt;/div&gt;&lt;/td&gt;
  &lt;td style="font-size: 11px; line-height: 1.4em; padding-left:
  20px; padding-top: 1px;" width="146"
  valign="top"&gt;&lt;div&gt;&lt;span style="color: #666666;
  font-size: 11px;"&gt;From:&lt;/span&gt; &lt;a
  href="http://www.youtube.com/profile?user=davidchoimusic"&gt;davidchoimusic&lt;/a&gt;&lt;/div&gt;
  &lt;div&gt;&lt;span style="color: #666666; font-size:
  11px;"&gt;Views:&lt;/span&gt; 113321&lt;/div&gt; &lt;div
  style="white-space: nowrap;text-align: left"&gt;&lt;img
  style="border: 0px none; margin: 0px; padding: 0px;
  vertical-align: middle; font-size: 11px;" align="top" alt=""
  src="http://gdata.youtube.com/static/images/icn_star_full_11x11.gif"&gt;
  &lt;img style="border: 0px none; margin: 0px; padding: 0px;
  vertical-align: middle; font-size: 11px;" align="top" alt=""
  src="http://gdata.youtube.com/static/images/icn_star_full_11x11.gif"&gt;
  &lt;img style="border: 0px none; margin: 0px; padding: 0px;
  vertical-align: middle; font-size: 11px;" align="top" alt=""
  src="http://gdata.youtube.com/static/images/icn_star_full_11x11.gif"&gt;
  &lt;img style="border: 0px none; margin: 0px; padding: 0px;
  vertical-align: middle; font-size: 11px;" align="top" alt=""
  src="http://gdata.youtube.com/static/images/icn_star_full_11x11.gif"&gt;
  &lt;img style="border: 0px none; margin: 0px; padding: 0px;
  vertical-align: middle; font-size: 11px;" align="top" alt=""
  src="http://gdata.youtube.com/static/images/icn_star_half_11x11.gif"&gt;&lt;/div&gt;
  &lt;div style="font-size: 11px;"&gt;1005 &lt;span style="color:
  #666666; font-size:
  11px;"&gt;ratings&lt;/span&gt;&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;
  &lt;tr&gt;&lt;td&gt;&lt;span style="color: #666666; font-size:
  11px;"&gt;Time:&lt;/span&gt; &lt;span style="color: #000000;
  font-size: 11px; font-weight:
  bold;"&gt;04:15&lt;/span&gt;&lt;/td&gt; &lt;td style="font-size:
  11px; padding-left: 20px;"&gt;&lt;span style="color: #666666;
  font-size: 11px;"&gt;More in&lt;/span&gt; &lt;a
  href="http://www.youtube.com/categories_portal?c=10"&gt;Music&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;</content>
  <link rel='self' type='application/atom+xml'
  href='http://gdata.youtube.com/feeds/videos/UMFI1hdm96E' />
  <link rel='alternate' type='text/html'
  href='http://www.youtube.com/watch?v=UMFI1hdm96E' />
  <link rel='http://gdata.youtube.com/schemas/2007#video.responses'
  type='application/atom+xml'
  href='http://gdata.youtube.com/feeds/videos/UMFI1hdm96E/responses' />
  <link rel='http://gdata.youtube.com/schemas/2007#video.related'
  type='application/atom+xml'
  href='http://gdata.youtube.com/feeds/videos/UMFI1hdm96E/related' />
  <author>
    <name>davidchoimusic</name>
    <uri>http://gdata.youtube.com/feeds/users/davidchoimusic</uri>
  </author>
  <media:group>
    <media:title type='plain'>"Crazy (Gnarles Barkley)" - Acoustic Cover</media:title>
    <media:description type='plain'>Gnarles Barkley acoustic cover http://www.myspace.com/davidchoimusic</media:description>
    <media:keywords>music, singing, gnarls, barkley, acoustic, cover</media:keywords>
    <yt:duration seconds='255' />
    <media:category label='Music'
    scheme='http://gdata.youtube.com/schemas/2007/categories.cat'>
    Music</media:category>
    <media:category 
    scheme='http://gdata.youtube.com/schemas/2007/developertags.cat'>
    DeveloperTag1</media:category>
    <media:content url='http://www.youtube.com/v/UMFI1hdm96E'
    type='application/x-shockwave-flash' medium='video'
    isDefault='true' expression='full' duration='255'
    yt:format='5' />
    <media:player url='http://www.youtube.com/watch?v=UMFI1hdm96E' />
    <media:thumbnail url='http://img.youtube.com/vi/UMFI1hdm96E/2.jpg'
    height='97' width='130' time='00:02:07.500' />
    <media:thumbnail url='http://img.youtube.com/vi/UMFI1hdm96E/1.jpg'
    height='97' width='130' time='00:01:03.750' />
    <media:thumbnail url='http://img.youtube.com/vi/UMFI1hdm96E/3.jpg'
    height='97' width='130' time='00:03:11.250' />
    <media:thumbnail url='http://img.youtube.com/vi/UMFI1hdm96E/0.jpg'
    height='240' width='320' time='00:02:07.500' />
    <yt:private />
  </media:group>
  <yt:statistics viewCount='113321' />
  <gd:rating min='1' max='5' numRaters='1005' average='4.77' />
  <georss:where>
    <gml:Point>
      <gml:pos>37.398529052734375 -122.0635986328125</gml:pos>
    </gml:Point>
  </georss:where>
  <gd:comments>
    <gd:feedLink href='http://gdata.youtube.com/feeds/videos/UMFI1hdm96E/comments' />
  </gd:comments>
  <yt:noembed />
      <app:control>
        <app:draft>yes</app:draft>
        <yt:state
          name="rejected"
          reasonCode="inappropriate"
          helpUrl="http://www.youtube.com/t/community_guidelines">
          The content of this video may violate the terms of use.</yt:state>
      </app:control>
</entry>"""

YOUTUBE_COMMENT_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'><id>http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments</id><updated>2008-05-19T21:45:45.261Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#comment'/><title type='text'>Comments</title><logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo><link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU'/><link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=2Idhz9ef5oU'/><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments?start-index=1&amp;max-results=25'/><author><name>YouTube</name><uri>http://www.youtube.com/</uri></author><generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator><openSearch:totalResults>0</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage>
  <entry>
    <id>http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/91F809A3DE2EB81B</id>
    <published>2008-02-22T15:27:15.000-08:00</published><updated>2008-02-22T15:27:15.000-08:00</updated>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#comment'/>
    <title type='text'>test66</title>
      <content type='text'>test66</content>
      <link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU'/>
      <link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=2Idhz9ef5oU'/>
      <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/91F809A3DE2EB81B'/>
      <author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author>
   </entry>
   <entry>
    <id>http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/A261AEEFD23674AA</id>
    <published>2008-02-22T15:27:01.000-08:00</published><updated>2008-02-22T15:27:01.000-08:00</updated>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#comment'/>
    <title type='text'>test333</title>
      <content type='text'>test333</content>
        <link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU'/>
        <link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=2Idhz9ef5oU'/>
        <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/A261AEEFD23674AA'/>
        <author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author>
    </entry>
    <entry>
      <id>http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/0DCF1E3531B3FF85</id>
      <published>2008-02-22T15:11:06.000-08:00</published><updated>2008-02-22T15:11:06.000-08:00</updated>
      <category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#comment'/>
      <title type='text'>test2</title>
      <content type='text'>test2</content>
        <link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU'/>
        <link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=2Idhz9ef5oU'/>
        <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2Idhz9ef5oU/comments/0DCF1E3531B3FF85'/>
        <author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author>
    </entry>
</feed>"""

YOUTUBE_PLAYLIST_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
    xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' 
    xmlns:media='http://search.yahoo.com/mrss/' 
    xmlns:yt='http://gdata.youtube.com/schemas/2007' 
    xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://gdata.youtube.com/feeds/users/andyland74/playlists?start-index=1&amp;max-results=25</id>
  <updated>2008-02-26T00:26:15.635Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#playlistLink'/>
  <title type='text'>andyland74's Playlists</title>
  <logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo>
  <link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/andyland74'/>
  <link rel='alternate' type='text/html' href='http://www.youtube.com/profile_play_list?user=andyland74'/>
  <link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/andyland74/playlists'/>
  <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/andyland74/playlists?start-index=1&amp;max-results=25'/>
  <author>
    <name>andyland74</name>
    <uri>http://gdata.youtube.com/feeds/users/andyland74</uri>
  </author>
  <generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>25</openSearch:itemsPerPage>
  <entry>
    <yt:description>My new playlist Description</yt:description>
    <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#playlist' href='http://gdata.youtube.com/feeds/playlists/8BCDD04DE8F771B2'/>
    <id>http://gdata.youtube.com/feeds/users/andyland74/playlists/8BCDD04DE8F771B2</id>
    <published>2007-11-04T17:30:27.000-08:00</published>
    <updated>2008-02-22T09:55:14.000-08:00</updated>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#playlistLink'/>
    <title type='text'>My New Playlist Title</title>
    <content type='text'>My new playlist Description</content>
    <link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/andyland74'/>
    <link rel='alternate' type='text/html' href='http://www.youtube.com/view_play_list?p=8BCDD04DE8F771B2'/>
    <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/andyland74/playlists/8BCDD04DE8F771B2'/>
    <author>
      <name>andyland74</name>                              
      <uri>http://gdata.youtube.com/feeds/users/andyland74</uri>
    </author>
  </entry>              
</feed>"""

YOUTUBE_PLAYLIST_VIDEO_FEED = """<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gml='http://www.opengis.net/gml' xmlns:georss='http://www.georss.org/georss' xmlns:media='http://search.yahoo.com/mrss/' xmlns:yt='http://gdata.youtube.com/schemas/2007' xmlns:gd='http://schemas.google.com/g/2005'><id>http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505</id><updated>2008-05-16T12:03:17.000-07:00</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#playlist'/><category scheme='http://gdata.youtube.com/schemas/2007/tags.cat' term='videos'/><category scheme='http://gdata.youtube.com/schemas/2007/tags.cat' term='python'/><title type='text'>Test Playlist</title><subtitle type='text'>Test playlist 1</subtitle><logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo><link rel='alternate' type='text/html' href='http://www.youtube.com/view_play_list?p=BCB3BB96DF51B505'/><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505?start-index=1&amp;max-results=25'/><author><name>gdpython</name><uri>http://gdata.youtube.com/feeds/api/users/gdpython</uri></author><generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator><openSearch:totalResults>1</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage><media:group><media:title type='plain'>Test Playlist</media:title><media:description type='plain'>Test playlist 1</media:description><media:content url='http://www.youtube.com/ep.swf?id=BCB3BB96DF51B505' type='application/x-shockwave-flash' yt:format='5'/></media:group><entry><id>http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505/B0F29389E537F888</id><updated>2008-05-16T20:54:08.520Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#playlist'/><title type='text'>Uploading YouTube Videos with the PHP Client Library</title><content type='text'>Jochen Hartmann demonstrates the basics of how to use the PHP Client Library with the YouTube Data API.

PHP Developer's Guide:
http://code.google.com/apis/youtube/developers_guide_php.html

Other documentation:
http://code.google.com/apis/youtube/</content><link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=iIp7OnHXBlo'/><link rel='http://gdata.youtube.com/schemas/2007#video.responses' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/iIp7OnHXBlo/responses'/><link rel='http://gdata.youtube.com/schemas/2007#video.related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/iIp7OnHXBlo/related'/><link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/videos/iIp7OnHXBlo'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505/B0F29389E537F888'/><author><name>GoogleDevelopers</name><uri>http://gdata.youtube.com/feeds/api/users/googledevelopers</uri></author><media:group><media:title type='plain'>Uploading YouTube Videos with the PHP Client Library</media:title><media:description type='plain'>Jochen Hartmann demonstrates the basics of how to use the PHP Client Library with the YouTube Data API.

PHP Developer's Guide:
http://code.google.com/apis/youtube/developers_guide_php.html

Other documentation:
http://code.google.com/apis/youtube/</media:description><media:keywords>api, data, demo, php, screencast, tutorial, uploading, walkthrough, youtube</media:keywords><yt:duration seconds='466'/><media:category label='Education' scheme='http://gdata.youtube.com/schemas/2007/categories.cat'>Education</media:category><media:content url='http://www.youtube.com/v/iIp7OnHXBlo' type='application/x-shockwave-flash' medium='video' isDefault='true' expression='full' duration='466' yt:format='5'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQlaBtdxOnuKiBMYDSANFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='466' yt:format='1'/><media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQlaBtdxOnuKiBMYESARFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='466' yt:format='6'/><media:player url='http://www.youtube.com/watch?v=iIp7OnHXBlo'/><media:thumbnail url='http://img.youtube.com/vi/iIp7OnHXBlo/2.jpg' height='97' width='130' time='00:03:53'/><media:thumbnail url='http://img.youtube.com/vi/iIp7OnHXBlo/1.jpg' height='97' width='130' time='00:01:56.500'/><media:thumbnail url='http://img.youtube.com/vi/iIp7OnHXBlo/3.jpg' height='97' width='130' time='00:05:49.500'/><media:thumbnail url='http://img.youtube.com/vi/iIp7OnHXBlo/0.jpg' height='240' width='320' time='00:03:53'/></media:group><yt:statistics viewCount='1550' favoriteCount='5'/><gd:rating min='1' max='5' numRaters='3' average='4.67'/><yt:location>undefined</yt:location><gd:comments><gd:feedLink href='http://gdata.youtube.com/feeds/api/videos/iIp7OnHXBlo/comments' countHint='2'/></gd:comments><yt:position>1</yt:position></entry></feed>"""

YOUTUBE_SUBSCRIPTION_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
    xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
    xmlns:media='http://search.yahoo.com/mrss/'
    xmlns:yt='http://gdata.youtube.com/schemas/2007'
    xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://gdata.youtube.com/feeds/users/andyland74/subscriptions?start-index=1&amp;max-results=25</id>
  <updated>2008-02-26T00:26:15.635Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://gdata.youtube.com/schemas/2007#subscription'/>
  <title type='text'>andyland74's Subscriptions</title>
  <logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo>
  <link rel='related' type='application/atom+xml'
    href='http://gdata.youtube.com/feeds/users/andyland74'/>
  <link rel='alternate' type='text/html'
    href='http://www.youtube.com/profile_subscriptions?user=andyland74'/>
  <link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml'
    href='http://gdata.youtube.com/feeds/users/andyland74/subscriptions'/>
  <link rel='self' type='application/atom+xml'
    href='http://gdata.youtube.com/feeds/users/andyland74/subscriptions?start-index=1&amp;max-results=25'/>
  <author>
    <name>andyland74</name>
    <uri>http://gdata.youtube.com/feeds/users/andyland74</uri>
  </author>
  <generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>25</openSearch:itemsPerPage>
  <entry>
    <id>http://gdata.youtube.com/feeds/users/andyland74/subscriptions/d411759045e2ad8c</id>
    <published>2007-11-04T17:30:27.000-08:00</published>
    <updated>2008-02-22T09:55:14.000-08:00</updated>
    <category scheme='http://gdata.youtube.com/schemas/2007/subscriptiontypes.cat'
      term='channel'/>
    <category scheme='http://schemas.google.com/g/2005#kind'
      term='http://gdata.youtube.com/schemas/2007#subscription'/>
    <title type='text'>Videos published by : NBC</title>
    <link rel='related' type='application/atom+xml'
      href='http://gdata.youtube.com/feeds/users/andyland74'/>
    <link rel='alternate' type='text/html'
      href='http://www.youtube.com/profile_videos?user=NBC'/>
    <link rel='self' type='application/atom+xml'
      href='http://gdata.youtube.com/feeds/users/andyland74/subscriptions/d411759045e2ad8c'/>
    <author>
      <name>andyland74</name>
      <uri>http://gdata.youtube.com/feeds/users/andyland74</uri>
    </author>
    <yt:username>NBC</yt:username>
    <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.uploads'
      href='http://gdata.youtube.com/feeds/api/users/nbc/uploads'/>
  </entry>
</feed>"""

YOUTUBE_VIDEO_RESPONSE_FEED = """<?xml version='1.0' encoding='UTF-8'?>
  <feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:gml='http://www.opengis.net/gml' xmlns:georss='http://www.georss.org/georss' xmlns:media='http://search.yahoo.com/mrss/' xmlns:yt='http://gdata.youtube.com/schemas/2007' xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://gdata.youtube.com/feeds/videos/2c3q9K4cHzY/responses</id><updated>2008-05-19T22:37:34.076Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#video'/><title type='text'>Videos responses to 'Giant NES controller coffee table'</title><logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo><link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2c3q9K4cHzY'/><link rel='alternate' type='text/html' href='http://www.youtube.com/video_response_view_all?v=2c3q9K4cHzY'/><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2c3q9K4cHzY/responses'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2c3q9K4cHzY/responses?start-index=1&amp;max-results=25'/><author><name>YouTube</name><uri>http://www.youtube.com/</uri></author><generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator><openSearch:totalResults>8</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage>
    <entry>
      <id>http://gdata.youtube.com/feeds/videos/7b9EnRI9VbY</id><published>2008-03-11T19:08:53.000-07:00</published><updated>2008-05-18T21:33:10.000-07:00</updated>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='OD'/><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#video'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='chat'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='Uncle'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='sex'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='catmint'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='kato'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='kissa'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='katt'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/categories.cat' term='Animals' label='Pets &amp; Animals'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='kat'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='cat'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='cats'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='kedi'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='gato'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='Brattman'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='drug'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='overdose'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='catnip'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='party'/>
      <category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='Katze'/><category scheme='http://gdata.youtube.com/schemas/2007/keywords.cat' term='gatto'/>
      <title type='text'>Catnip Party</title><content type='html'>snipped</content>
      <link rel='alternate' type='text/html' href='http://www.youtube.com/watch?v=7b9EnRI9VbY'/>
      <link rel='http://gdata.youtube.com/schemas/2007#video.responses' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/7b9EnRI9VbY/responses'/>
      <link rel='http://gdata.youtube.com/schemas/2007#video.related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/7b9EnRI9VbY/related'/>
      <link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/videos/2c3q9K4cHzY/responses/7b9EnRI9VbY'/>
      <author><name>PismoBeach</name><uri>http://gdata.youtube.com/feeds/users/pismobeach</uri></author>
        <media:group>
          <media:title type='plain'>Catnip Party</media:title>
          <media:description type='plain'>Uncle, Hillary, Hankette, and B4 all but overdose on the patio</media:description><media:keywords>Brattman, cat, catmint, catnip, cats, chat, drug, gato, gatto, kat, kato, katt, Katze, kedi, kissa, OD, overdose, party, sex, Uncle</media:keywords>
          <yt:duration seconds='139'/>
          <media:category label='Pets &amp; Animals' scheme='http://gdata.youtube.com/schemas/2007/categories.cat'>Animals</media:category>
          <media:content url='http://www.youtube.com/v/7b9EnRI9VbY' type='application/x-shockwave-flash' medium='video' isDefault='true' expression='full' duration='139' yt:format='5'/>
          <media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQm2VT0SnUS_7RMYDSANFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='139' yt:format='1'/>
          <media:content url='rtsp://rtsp2.youtube.com/ChoLENy73wIaEQm2VT0SnUS_7RMYESARFEgGDA==/0/0/0/video.3gp' type='video/3gpp' medium='video' expression='full' duration='139' yt:format='6'/>
          <media:player url='http://www.youtube.com/watch?v=7b9EnRI9VbY'/>
          <media:thumbnail url='http://img.youtube.com/vi/7b9EnRI9VbY/2.jpg' height='97' width='130' time='00:01:09.500'/>
          <media:thumbnail url='http://img.youtube.com/vi/7b9EnRI9VbY/1.jpg' height='97' width='130' time='00:00:34.750'/>
          <media:thumbnail url='http://img.youtube.com/vi/7b9EnRI9VbY/3.jpg' height='97' width='130' time='00:01:44.250'/>
          <media:thumbnail url='http://img.youtube.com/vi/7b9EnRI9VbY/0.jpg' height='240' width='320' time='00:01:09.500'/>
        </media:group>
        <yt:statistics viewCount='4235' favoriteCount='3'/>
        <gd:rating min='1' max='5' numRaters='24' average='3.54'/>
        <gd:comments>
          <gd:feedLink href='http://gdata.youtube.com/feeds/videos/7b9EnRI9VbY/comments' countHint='14'/>
        </gd:comments>
        </entry>
</feed>
"""


YOUTUBE_PROFILE = """<?xml version='1.0' encoding='UTF-8'?>
<entry xmlns='http://www.w3.org/2005/Atom'
    xmlns:media='http://search.yahoo.com/mrss/'
    xmlns:yt='http://gdata.youtube.com/schemas/2007'
    xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://gdata.youtube.com/feeds/users/andyland74</id>
  <published>2006-10-16T00:09:45.000-07:00</published>
  <updated>2008-02-26T11:48:21.000-08:00</updated>
  <category scheme='http://gdata.youtube.com/schemas/2007/channeltypes.cat'
    term='Standard'/>
  <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://gdata.youtube.com/schemas/2007#userProfile'/>
  <title type='text'>andyland74 Channel</title>
  <link rel='alternate' type='text/html'
    href='http://www.youtube.com/profile?user=andyland74'/>
  <link rel='self' type='application/atom+xml'
    href='http://gdata.youtube.com/feeds/users/andyland74'/>
  <author>
    <name>andyland74</name>
    <uri>http://gdata.youtube.com/feeds/users/andyland74</uri>
  </author>
  <yt:age>33</yt:age>
  <yt:username>andyland74</yt:username>
  <yt:firstName>andy</yt:firstName>
  <yt:lastName>example</yt:lastName>
  <yt:books>Catch-22</yt:books>
  <yt:gender>m</yt:gender>
  <yt:company>Google</yt:company>
  <yt:hobbies>Testing YouTube APIs</yt:hobbies>
  <yt:hometown>Somewhere</yt:hometown>
  <yt:location>US</yt:location>
  <yt:movies>Aqua Teen Hungerforce</yt:movies>
  <yt:music>Elliott Smith</yt:music>
  <yt:occupation>Technical Writer</yt:occupation>
  <yt:school>University of North Carolina</yt:school>
  <media:thumbnail url='http://i.ytimg.com/vi/YFbSxcdOL-w/default.jpg'/>
  <yt:statistics viewCount='9' videoWatchCount='21' subscriberCount='1'
    lastWebAccess='2008-02-25T16:03:38.000-08:00'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.favorites'
    href='http://gdata.youtube.com/feeds/users/andyland74/favorites' countHint='4'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.contacts'
    href='http://gdata.youtube.com/feeds/users/andyland74/contacts' countHint='1'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.inbox'
    href='http://gdata.youtube.com/feeds/users/andyland74/inbox' countHint='0'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.playlists'
    href='http://gdata.youtube.com/feeds/users/andyland74/playlists'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.subscriptions'
    href='http://gdata.youtube.com/feeds/users/andyland74/subscriptions' countHint='4'/>
  <gd:feedLink rel='http://gdata.youtube.com/schemas/2007#user.uploads'
    href='http://gdata.youtube.com/feeds/users/andyland74/uploads' countHint='1'/>
</entry>"""

YOUTUBE_CONTACTS_FEED = """<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:yt='http://gdata.youtube.com/schemas/2007' xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts</id><updated>2008-05-16T19:24:34.916Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#friend'/><title type='text'>apitestjhartmann's Contacts</title><logo>http://www.youtube.com/img/pic_youtubelogo_123x63.gif</logo><link rel='alternate' type='text/html' href='http://www.youtube.com/profile_friends?user=apitestjhartmann'/><link rel='http://schemas.google.com/g/2005#feed' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts'/><link rel='http://schemas.google.com/g/2005#post' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts?start-index=1&amp;max-results=25'/><author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author><generator version='beta' uri='http://gdata.youtube.com/'>YouTube data API</generator><openSearch:totalResults>2</openSearch:totalResults><openSearch:startIndex>1</openSearch:startIndex><openSearch:itemsPerPage>25</openSearch:itemsPerPage>
    <entry>
      <id>http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/test89899090</id><published>2008-02-04T11:27:54.000-08:00</published><updated>2008-05-16T19:24:34.916Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#friend'/><title type='text'>test89899090</title><link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/test89899090'/><link rel='alternate' type='text/html' href='http://www.youtube.com/profile?user=test89899090'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/test89899090'/><link rel='edit' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/test89899090'/><author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author><yt:username>test89899090</yt:username><yt:status>requested</yt:status></entry>
    <entry>
      <id>http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/testjfisher</id><published>2008-02-26T14:13:03.000-08:00</published><updated>2008-05-16T19:24:34.916Z</updated><category scheme='http://schemas.google.com/g/2005#kind' term='http://gdata.youtube.com/schemas/2007#friend'/><title type='text'>testjfisher</title><link rel='related' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/testjfisher'/><link rel='alternate' type='text/html' href='http://www.youtube.com/profile?user=testjfisher'/><link rel='self' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/testjfisher'/><link rel='edit' type='application/atom+xml' href='http://gdata.youtube.com/feeds/users/apitestjhartmann/contacts/testjfisher'/><author><name>apitestjhartmann</name><uri>http://gdata.youtube.com/feeds/users/apitestjhartmann</uri></author><yt:username>testjfisher</yt:username><yt:status>pending</yt:status></entry>
</feed>"""


NEW_CONTACT = """<?xml version='1.0' encoding='UTF-8'?>
<atom:entry xmlns:atom='http://www.w3.org/2005/Atom'
    xmlns:gd='http://schemas.google.com/g/2005'>
  <atom:category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/contact/2008#contact' />
  <atom:title type='text'>Elizabeth Bennet</atom:title>
  <atom:content type='text'>Notes</atom:content>
  <gd:email rel='http://schemas.google.com/g/2005#work'
    address='liz@gmail.com' />
  <gd:email rel='http://schemas.google.com/g/2005#home'
    address='liz@example.org' />
  <gd:phoneNumber rel='http://schemas.google.com/g/2005#work'
    primary='true'>(206)555-1212</gd:phoneNumber>
  <gd:phoneNumber rel='http://schemas.google.com/g/2005#home'>(206)555-1213</gd:phoneNumber>
  <gd:im address='liz@gmail.com'
    protocol='http://schemas.google.com/g/2005#GOOGLE_TALK'
    rel='http://schemas.google.com/g/2005#home' />
  <gd:postalAddress rel='http://schemas.google.com/g/2005#work'
    primary='true'>1600 Amphitheatre Pkwy Mountain View</gd:postalAddress>
</atom:entry>"""

CONTACTS_FEED = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom'
    xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/'
    xmlns:gd='http://schemas.google.com/g/2005'>
  <id>http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base</id>
  <updated>2008-03-05T12:36:38.836Z</updated>
  <category scheme='http://schemas.google.com/g/2005#kind'
    term='http://schemas.google.com/contact/2008#contact' />
  <title type='text'>Contacts</title>
  <link rel='http://schemas.google.com/g/2005#feed'
    type='application/atom+xml'
    href='http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base' />
  <link rel='http://schemas.google.com/g/2005#post'
    type='application/atom+xml'
    href='http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base' />
  <link rel='self' type='application/atom+xml'
    href='http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base?max-results=25' />
  <author>
    <name>Elizabeth Bennet</name>
    <email>liz@gmail.com</email>
  </author>
  <generator version='1.0' uri='http://www.google.com/m8/feeds/contacts'>Contacts</generator>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>25</openSearch:itemsPerPage>
  <entry>
    <id>http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base/c9012de</id>
    <updated>2008-03-05T12:36:38.835Z</updated>
    <category scheme='http://schemas.google.com/g/2005#kind'
      term='http://schemas.google.com/contact/2008#contact' />
    <title type='text'>Fitzgerald</title>
    <link rel='self' type='application/atom+xml'
      href='http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base/c9012de' />
    <link rel='edit' type='application/atom+xml'
      href='http://www.google.com/m8/feeds/contacts/liz%40gmail.com/base/c9012de/1204720598835000' />
    <gd:phoneNumber rel='http://schemas.google.com/g/2005#home'
      primary='true'>456</gd:phoneNumber>
  </entry>
</feed>"""

BLOG_ENTRY = """<entry xmlns='http://www.w3.org/2005/Atom'>
  <id>tag:blogger.com,1999:blog-blogID.post-postID</id>
  <published>2006-08-02T18:44:43.089-07:00</published>
  <updated>2006-11-08T18:10:23.020-08:00</updated>
  <title type='text'>Lizzy's Diary</title>
  <summary type='html'>Being the journal of Elizabeth Bennet</summary>
  <link rel='alternate' type='text/html'
    href='http://blogName.blogspot.com/'>
  </link>
  <link rel='http://schemas.google.com/g/2005#feed'
    type='application/atom+xml'
    href='http://blogName.blogspot.com/feeds/posts/default'>
  </link>
  <link rel='http://schemas.google.com/g/2005#post'
    type='application/atom+xml'
    href='http://www.blogger.com/feeds/blogID/posts/default'>
  </link>
  <link rel='self' type='application/atom+xml'
    href='http://www.blogger.com/feeds/userID/blogs/blogID'>
  </link>
  <link rel='edit' type='application/atom+xml' 
      href='http://www.blogger.com/feeds/userID/blogs/blogID'>
  </link>
  <author>
    <name>Elizabeth Bennet</name>
    <email>liz@gmail.com</email>
  </author>
</entry>"""

BLOG_POST = """<entry xmlns='http://www.w3.org/2005/Atom'>
  <title type='text'>Marriage!</title>
  <content type='xhtml'>
    <div xmlns="http://www.w3.org/1999/xhtml">
      <p>Mr. Darcy has <em>proposed marriage</em> to me!</p>
      <p>He is the last man on earth I would ever desire to marry.</p>
      <p>Whatever shall I do?</p>
    </div>
  </content>
  <author>
    <name>Elizabeth Bennet</name>
    <email>liz@gmail.com</email>
  </author>
</entry>"""

BLOG_POSTS_FEED = """<feed xmlns='http://www.w3.org/2005/Atom'>
  <id>tag:blogger.com,1999:blog-blogID</id>
  <updated>2006-11-08T18:10:23.020-08:00</updated>
  <title type='text'>Lizzy's Diary</title>
  <link rel='alternate' type='text/html'
    href='http://blogName.blogspot.com/index.html'>
  </link>
  <link rel='http://schemas.google.com/g/2005#feed'
    type='application/atom+xml'
    href='http://blogName.blogspot.com/feeds/posts/default'>
  </link>
  <link rel='self' type='application/atom+xml'
    href='http://blogName.blogspot.com/feeds/posts/default'>
  </link>
  <author>
    <name>Elizabeth Bennet</name>
    <email>liz@gmail.com</email>
  </author>
  <generator version='7.00' uri='http://www2.blogger.com'>Blogger</generator>
  <entry>
    <id>tag:blogger.com,1999:blog-blogID.post-postID</id>
    <published>2006-11-08T18:10:00.000-08:00</published>
    <updated>2006-11-08T18:10:14.954-08:00</updated>
    <title type='text'>Quite disagreeable</title>
    <content type='html'>&lt;p&gt;I met Mr. Bingley's friend Mr. Darcy
      this evening. I found him quite disagreeable.&lt;/p&gt;</content>
    <link rel='alternate' type='text/html'
      href='http://blogName.blogspot.com/2006/11/quite-disagreeable.html'>
    </link>
    <link rel='self' type='application/atom+xml'
      href='http://blogName.blogspot.com/feeds/posts/default/postID'>
    </link>
    <link rel='edit' type='application/atom+xml'
      href='http://www.blogger.com/feeds/blogID/posts/default/postID'>
    </link>
    <author>
      <name>Elizabeth Bennet</name>
      <email>liz@gmail.com</email>
    </author>
  </entry>
</feed>"""

BLOG_COMMENTS_FEED = """<feed xmlns="http://www.w3.org/2005/Atom" xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/">
  <id>tag:blogger.com,1999:blog-blogID.postpostID..comments</id>
  <updated>2007-04-04T21:56:29.803-07:00</updated>
  <title type="text">My Blog : Time to relax</title>
  <link rel="alternate" type="text/html" href="http://blogName.blogspot.com/2007/04/first-post.html"/>
  <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml" href="http://blogName.blogspot.com/feeds/postID/comments/default"/>
  <link rel="self" type="application/atom+xml" href="http://blogName.blogspot.com/feeds/postID/comments/default"/>
  <author>
    <name>Blog Author name</name>
  </author>
  <generator version="7.00" uri="http://www2.blogger.com">Blogger</generator>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <entry>
    <id>tag:blogger.com,1999:blog-blogID.post-commentID</id>
    <published>2007-04-04T21:56:00.000-07:00</published>
    <updated>2007-04-04T21:56:29.803-07:00</updated>
    <title type="text">This is my first comment</title>
    <content type="html">This is my first comment</content>
    <link rel="alternate" type="text/html" href="http://blogName.blogspot.com/2007/04/first-post.html#commentID"/>
    <link rel="self" type="application/atom+xml" href="http://blogName.blogspot.com/feeds/postID/comments/default/commentID"/>
    <link rel="edit" type="application/atom+xml" href="http://www.blogger.com/feeds/blogID/postID/comments/default/commentID"/>
    <author>
      <name>Blog Author name</name>
    </author>
  </entry>
</feed>"""
