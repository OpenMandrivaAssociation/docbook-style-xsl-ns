%define Name docbook-style-xsl-ns

Name:		%{Name}
Version:	1.78.1
Release:	3
Group:		Publishing

Summary:	Norman Walsh's modular stylesheets for DocBook5

License:	Artistic style
URL:		http://sourceforge.net/projects/docbook

Provides:	docbook-xsl = %{version}
Requires:	docbook-dtd-xml
Requires(pre):	sgml-common >= 0.6.3-2mdk
# BuildRequires:	gcj-tools
Source0:	https://sourceforge.net/projects/docbook/files/docbook-xsl-ns/1.78.1/docbook-xsl-ns-%{version}.tar.bz2
BuildArch:	noarch
Obsoletes:	docbook5-style-xsl
Provides:	docbook5-style-xsl

%define sgmlbase %{_datadir}/sgml/

%Description
These XSL stylesheets allow to convert any DocBook5 document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.
Note that this is an experimental release for testing purposes only: it makes
the stylesheets namespace aware for the first time for DocBook 5 (RNG based).
For production use please install docbook-style-xsl instead.

%prep
%setup -n docbook-xsl-ns-%{version} -q

%build
# index jar files to please rpmlint
# jar -i extensions/*.jar

%install
TARGET=%{sgmlbase}/docbook/xsl-stylesheets-db5-%{version}
mkdir -p %{buildroot}$TARGET
# Camille 2007-01-23: "slides website roundtrip" XSL not available in this DB5 release
cp -a VERSION common eclipse extensions fo highlighting html htmlhelp images javahelp lib template xhtml manpages profiling params tools %{buildroot}$TARGET


%files
%doc BUGS TODO README VERSION NEWS* COPYING RELEASE* INSTALL
%{sgmlbase}/docbook/xsl-stylesheets-db5-%{version}
