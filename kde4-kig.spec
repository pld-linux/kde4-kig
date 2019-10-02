%define		_state		stable
%define		orgname		kig

Summary:	K Desktop Environment - Interactive Geometry
Summary(pl.UTF-8):	K Desktop Environment - Interaktywna geometria
Name:		kde4-kig
Version:	4.14.3
Release:	8
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2bc36c90f19b9fbebd7b3c7ac563acb3
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	boost-python-devel
BuildRequires:	kde4-kdelibs-devel >= 4
BuildRequires:	python-devel >= 2
BuildRequires:	qt4-build >= 4
BuildRequires:	sed >= 4.0
Obsoletes:	kde4-kdeedu-kig < 4.6.99
Obsoletes:	kig <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kig is an application for Interactive Geometry. It's intended to serve
two purposes:
- allow students to interactively explore mathematical figures and
  concepts using the computer.
- serve as a WYSIWYG tool for drawing mathematical figures and
  including them in other documents.

%description -l pl.UTF-8
Kig to aplikacja do interaktywnej geometrii. Ma służyć dwóm celom:
- umożliwić uczniom interaktywnie przeglądanie figur i pojęć
  matematycznych przy użyciu komputera
- służyć jako narzędzie WYSIWYG do rysowania figur matematycznych i
  włączania ich do innych dokumentów.

%prep
%setup -q -n %{orgname}-%{version}

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' pykig/pykig.py

%build
install -d build
cd build
%cmake .. \
	-DBoostPython_INCLUDE_DIRS=%{py_incdir} \
	-DBoostPython_LIBRARIES="boost_python%(echo %{py_ver} | tr -d .);python%{py_ver}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kig
%attr(755,root,root) %{_bindir}/pykig.py
%attr(755,root,root) %{_libdir}/kde4/kigpart.so
%{_datadir}/appdata/kig.appdata.xml
%{_datadir}/apps/kig
%{_datadir}/kde4/services/kig_part.desktop
%{_desktopdir}/kde4/kig.desktop
%{_iconsdir}/hicolor/*x*/apps/kig.png
%{_iconsdir}/hicolor/scalable/apps/kig.svgz
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-kig.svgz
%{_mandir}/man1/kig.1*

# subpackage?
%{_datadir}/apps/katepart/syntax/python-kig.xml
