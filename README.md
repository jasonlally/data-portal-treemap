Open Data Browser
==============

A zoomable treemap of [Socrata based data catalogs](http://www.socrata.com), with the datasets grouped by categories (defined by the portal) and dimensions drawn based on the size of the individual datasets. Currently the color simply helps keep the rectangles distinct, but in future versions information (e.g. # of views the dataset has received, or tags from the portal) could be encoded in a color scale. The rectangles are linked to the datasets they represent in the portal (just click anywhere within the rectangle).

This project builds off of the initial work done by [Paul Meinshausen](https://github.com/PMeinshausen) with contributions from [Nick Doiron](https://github.com/mapmeld) on [Chicago](https://github.com/dssg/data-portal-treemap) and [Boston](https://github.com/mapmeld/data-portal-treemap) data.
                                    
The d3 code is heavily based on code shared by [The Ohio State University Department of Political Science](https://secure.polisci.ohio-state.edu/faq/d3/zoomabletreemap_code.php)

##Contributing
Currently happy to have contributors. There's an empty issue queue that needs filling.  There will soon be a clearer roadmap that includes:
-Adding CKAN catalogs
-Adding stats on each of the catalogs
-Representing non-tabular data (like GIS shapefiles)
-Adding a list of the datasets that will update as your click through the treemap
