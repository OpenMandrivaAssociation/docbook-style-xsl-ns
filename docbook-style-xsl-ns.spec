%define Name docbook-style-xsl-ns

Name:		%{Name}
Version:	1.79.1
Release:	5
Group:		Publishing
Summary:	Norman Walsh's modular stylesheets for DocBook5
License:	Artistic style
URL:		https://sourceforge.net/projects/docbook
Provides:	docbook-xsl-ns = %{version}
Requires:	docbook-dtd-xml
Requires(pre):	sgml-common >= 0.6.3-2mdk
Source0:	https://sourceforge.net/projects/docbook/files/docbook-xsl-ns/1.79.1/docbook-xsl-ns-%{version}.tar.bz2
BuildArch:	noarch
%rename		docbook5-style-xsl

%define sgmlbase %{_datadir}/sgml/

%Description
These XSL stylesheets allow to convert any DocBook5 document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.
Note that this is an experimental release for testing purposes only: it makes
the stylesheets namespace aware for the first time for DocBook 5 (RNG based).
For production use please install docbook-style-xsl instead.

%prep
%autosetup -n docbook-xsl-ns-%{version} -p1

%build
# index jar files to please rpmlint
# jar -i extensions/*.jar

%install
TARGET=%{sgmlbase}/docbook/xsl-ns-stylesheets-%{version}
mkdir -p %{buildroot}$TARGET
# Camille 2007-01-23: "slides website roundtrip" XSL not available in this DB5 release
cp -a VERSION common eclipse extensions fo highlighting html htmlhelp images javahelp lib template xhtml manpages profiling params tools %{buildroot}$TARGET
ln -s VERSION %{buildroot}$TARGET/VERSION.xsl

ln -s xsl-ns-stylesheets-%{version} \
%{buildroot}/%{sgmlbase}/docbook/xsl-ns-stylesheets

%post
CATALOG=/etc/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
	"http://docbook.sourceforge.net/release/xsl-ns/%{version}" \
	"file:///usr/share/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
	"http://docbook.sourceforge.net/release/xsl-ns/%{version}" \
	"file:///usr/share/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
	"http://docbook.sourceforge.net/release/xsl-ns/current" \
	"file:///usr/share/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
	"http://docbook.sourceforge.net/release/xsl-ns/current" \
	"file:///usr/share/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%postun
# do not remove on upgrade
CATALOG=/etc/xml/catalog
if [ "$1" = "0" -a -x %{_bindir}/xmlcatalog -a -f $CATALOG ]; then
  %{_bindir}/xmlcatalog --noout --del \
	"file:///usr/share/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
fi

%files
%doc BUGS TODO README VERSION NEWS* COPYING RELEASE* INSTALL
%{sgmlbase}/docbook/xsl-ns-stylesheets-%{version}
%{sgmlbase}/docbook/xsl-ns-stylesheets
