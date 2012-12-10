%define Name docbook-style-xsl-ns
%define version 1.75.2
%define Release %mkrel 3

Name:		%{Name}
Version:	%{version}
Release:	%mkrel 2
Group:		Publishing

Summary:	Norman Walsh's modular stylesheets for DocBook5

License:	Artistic style
URL:		http://sourceforge.net/projects/docbook

Provides:	docbook-xsl = %{version}
Requires:	docbook-dtd-xml
Requires(pre):	sgml-common >= 0.6.3-2mdk
# BuildRequires:	gcj-tools

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot 

Source0:	http://prdownloads.sourceforge.net/docbook/docbook-xsl-ns-%{version}.tar.bz2

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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT$TARGET
# Camille 2007-01-23: "slides website roundtrip" XSL not available in this DB5 release
cp -a VERSION common eclipse extensions fo highlighting html htmlhelp images javahelp lib template xhtml manpages profiling params tools $RPM_BUILD_ROOT$TARGET

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-,root,root)
%doc BUGS TODO README VERSION NEWS* COPYING RELEASE* INSTALL
%{sgmlbase}/docbook/xsl-stylesheets-db5-%{version}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.75.2-2mdv2011.0
+ Revision: 617867
- the mass rebuild of 2010.0 packages

* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 1.75.2-1mdv2010.0
+ Revision: 417410
- Use %%mkrel
- update to new version 1.75.2

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.73.2-3mdv2009.0
+ Revision: 240632
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 1.73.2-1mdv2008.0
+ Revision: 76413
- Obsoletes old name
- New versino 1.73.2
- docbook5-xsl renamed to docbook-style-ns


* Wed Jan 24 2007 Camille Bégnis <camille@mandriva.com> 1.72.0-1mdv2007.0
+ Revision: 112876
- simplify spec
- Import docbook5-style-xsl

* Wed Jan 24 2007 Camille Begnis <camille@mandriva.com> 1.72.0-1mdv2007.1
- Esperimental stylesheet release for native (namespaced) DocBook5 support

