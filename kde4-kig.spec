%define		_state		stable
%define		orgname		kig

Summary:	K Desktop Environment - Interactive Geometry
Summary(pl_PL.UTF8):	K Desktop Environment - Interaktywna geometria
Name:		kig
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	d470977abb051c738bd2cf7d54b50553
URL:		http://www.kde.org/
BuildRequires:	boost-python-devel
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-kig < 4.6.99
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

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pykig.py
%attr(755,root,root) %{_libdir}/kde4/kigpart.so
%attr(755,root,root) %{_bindir}/kig
%{_desktopdir}/kde4/kig.desktop
%{_datadir}/kde4/services/kig_part.desktop
%{_datadir}/apps/kig
%{_iconsdir}/hicolor/*x*/apps/kig.png
%{_iconsdir}/hicolor/scalable/apps/kig.svgz
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-kig.svgz
%{_mandir}/man1/kig.1*

# subpackage?
%{_datadir}/apps/katepart/syntax/python-kig.xml