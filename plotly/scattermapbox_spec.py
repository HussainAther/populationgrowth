'data': [{
           'type': 'scattermapbox',
           'lat': lat, 'lon': lon,
       }],
'layout': {
           'mapbox': {
		   ...
               'layers': [{
               "sourcetype": "image",
               "source": datashader_output_img,
      	}],
}
