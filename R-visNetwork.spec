#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-visNetwork
Version  : 2.1.0
Release  : 43
URL      : https://cran.r-project.org/src/contrib/visNetwork_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/visNetwork_2.1.0.tar.gz
Summary  : Network Visualization using 'vis.js' Library
Group    : Development/Tools
License  : MIT
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-magrittr
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : buildreq-R

%description
library. It allows an interactive visualization of networks.

%prep
%setup -q -c -n visNetwork
cd %{_builddir}/visNetwork

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632926940

%install
export SOURCE_DATE_EPOCH=1632926940
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library visNetwork
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library visNetwork
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library visNetwork
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc visNetwork || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/visNetwork/DESCRIPTION
/usr/lib64/R/library/visNetwork/INDEX
/usr/lib64/R/library/visNetwork/LICENSE
/usr/lib64/R/library/visNetwork/Meta/Rd.rds
/usr/lib64/R/library/visNetwork/Meta/features.rds
/usr/lib64/R/library/visNetwork/Meta/hsearch.rds
/usr/lib64/R/library/visNetwork/Meta/links.rds
/usr/lib64/R/library/visNetwork/Meta/nsInfo.rds
/usr/lib64/R/library/visNetwork/Meta/package.rds
/usr/lib64/R/library/visNetwork/Meta/vignette.rds
/usr/lib64/R/library/visNetwork/NAMESPACE
/usr/lib64/R/library/visNetwork/NEWS
/usr/lib64/R/library/visNetwork/NOTICE
/usr/lib64/R/library/visNetwork/R/visNetwork
/usr/lib64/R/library/visNetwork/R/visNetwork.rdb
/usr/lib64/R/library/visNetwork/R/visNetwork.rdx
/usr/lib64/R/library/visNetwork/common-docs-files/css/carousel.css
/usr/lib64/R/library/visNetwork/common-docs-files/css/style.css
/usr/lib64/R/library/visNetwork/common-docs-files/js/ie-emulation-modes-warning.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/ie10-viewport-bug-workaround.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/jquery.highlight.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/jquery.url.min.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/main.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/tipuesearch.config.js
/usr/lib64/R/library/visNetwork/common-docs-files/js/toggleTable.js
/usr/lib64/R/library/visNetwork/doc/Introduction-to-visNetwork.R
/usr/lib64/R/library/visNetwork/doc/Introduction-to-visNetwork.Rmd
/usr/lib64/R/library/visNetwork/doc/Introduction-to-visNetwork.html
/usr/lib64/R/library/visNetwork/doc/index.html
/usr/lib64/R/library/visNetwork/docjs/css/overrides.css
/usr/lib64/R/library/visNetwork/docjs/network/configure.html
/usr/lib64/R/library/visNetwork/docjs/network/edges.html
/usr/lib64/R/library/visNetwork/docjs/network/groups.html
/usr/lib64/R/library/visNetwork/docjs/network/index.html
/usr/lib64/R/library/visNetwork/docjs/network/interaction.html
/usr/lib64/R/library/visNetwork/docjs/network/layout.html
/usr/lib64/R/library/visNetwork/docjs/network/manipulation.html
/usr/lib64/R/library/visNetwork/docjs/network/nodes.html
/usr/lib64/R/library/visNetwork/docjs/network/physics.html
/usr/lib64/R/library/visNetwork/fontAwesome/Font_Awesome_Cheatsheet_4_7_0.pdf
/usr/lib64/R/library/visNetwork/help/AnIndex
/usr/lib64/R/library/visNetwork/help/aliases.rds
/usr/lib64/R/library/visNetwork/help/paths.rds
/usr/lib64/R/library/visNetwork/help/visNetwork.rdb
/usr/lib64/R/library/visNetwork/help/visNetwork.rdx
/usr/lib64/R/library/visNetwork/html/00Index.html
/usr/lib64/R/library/visNetwork/html/R.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/css/dataManipulation.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/Blob/Blob.js
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/Blob/LICENSE.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/Blob/README.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/FileSaver/FileSaver.min.js
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/FileSaver/LICENSE.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/FileSaver/README.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/canvas-toBlob/LICENSE.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/canvas-toBlob/README.md
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/canvas-toBlob/canvas-toBlob.js
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/html2canvas/html2canvas.js
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/export/jsPDF/jspdf.debug.js
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/css/font-awesome.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/css/font-awesome.css.map
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/css/font-awesome.min.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/FontAwesome.otf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/fontawesome-webfont.eot
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/fontawesome-webfont.svg
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/fontawesome-webfont.ttf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/fontawesome-webfont.woff
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/fonts/fontawesome-webfont.woff2
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/animated.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/bordered-pulled.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/core.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/fixed-width.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/font-awesome.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/icons.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/larger.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/list.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/mixins.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/path.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/rotated-flipped.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/screen-reader.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/stacked.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/less/variables.less
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_animated.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_bordered-pulled.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_core.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_fixed-width.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_icons.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_larger.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_list.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_mixins.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_path.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_rotated-flipped.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_screen-reader.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_stacked.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/_variables.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_4.7.0/scss/font-awesome.scss
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/LICENSE.txt
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/css/all.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/css/all.min.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-brands-400.eot
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-brands-400.svg
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-brands-400.ttf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-brands-400.woff
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-brands-400.woff2
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-regular-400.eot
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-regular-400.svg
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-regular-400.ttf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-regular-400.woff
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-regular-400.woff2
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-solid-900.eot
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-solid-900.svg
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-solid-900.ttf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-solid-900.woff
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/fontawesome_5.13.0/webfonts/fa-solid-900.woff2
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/LICENSE
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/css/ionicons.min.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/fonts/ionicons.eot
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/fonts/ionicons.svg
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/fonts/ionicons.ttf
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/ionicons/fonts/ionicons.woff
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/add_css.txt
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/acceptDeleteIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/addNodeIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/backIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/connectIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/cross.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/cross2.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/deleteIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/downArrow.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/editIcon.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/leftArrow.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/minus.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/plus.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/rightArrow.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/upArrow.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/img/network/zoomExtends.png
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/vis-network.min.css
/usr/lib64/R/library/visNetwork/htmlwidgets/lib/vis/vis-network.min.js
/usr/lib64/R/library/visNetwork/htmlwidgets/visNetwork.js
/usr/lib64/R/library/visNetwork/htmlwidgets/visNetwork.yaml
/usr/lib64/R/library/visNetwork/img/tree_example.png
/usr/lib64/R/library/visNetwork/shiny/server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/basic_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/manip_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/options_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_anim_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_get_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_nodes_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_options_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_select_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_set_title_server.R
/usr/lib64/R/library/visNetwork/shiny/src/server/proxy_update_server.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/basic_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/manip_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/options_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_anim_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_get_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_nodes_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_options_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_select_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_set_title_ui.R
/usr/lib64/R/library/visNetwork/shiny/src/ui/proxy_update_ui.R
/usr/lib64/R/library/visNetwork/shiny/ui.R
/usr/lib64/R/library/visNetwork/tests/highlight_combinaison.R
/usr/lib64/R/library/visNetwork/tests/understand_coordinates.R
