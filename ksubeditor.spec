#TODO - polish translation
%define rcver	rc1

Summary:	Ksubeditor is a DivX subtitle editor for KDE 3.x
Summary(pl):	Ksubeditor jest edytorem napisów dla KDE 3.x
Name:		ksubeditor
Version:	0.2
Release:	0.%{rcver}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}%{rcver}.tar.gz
# Source0-md5:	dfcfa14178f12540f53836036fa97980
URL:		http://www.sourceforge.net/projects/ksubeditor/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksubeditor is a DivX subtitle editor for KDE 3.x. It is able to edit
and convert subtitles between different subtitle formats. It is able
to easily change the time of the subtitle and fit it to the movie.

%description -l pl
Ksubeditor jest edytorem napisów dla KDE 3.x. Jest w stanie
modyfikowaæ oraz konwertowaæ napisy pomiêdzy ró¿nymi formatami. Mo¿e w
prosty sposób zmieniaæ czas napisów oraz dopasowaæ je do filmu.

%prep
%setup -q -n %{name}-%{version}%{rcver}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_pixmapsdir}/locolor/{16x16,32x32},%{_bindir}}

install ksubeditor/lo16-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16
install ksubeditor/lo32-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/32x32
install ksubeditor/ksubeditor $RPM_BUILD_ROOT%{_bindir}
install ksubeditor/ksubeditor.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/locolor/16x16/*
%{_pixmapsdir}/locolor/32x32/*
%{_applnkdir}/Utilities/ksubeditor.desktop
