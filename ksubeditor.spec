#TODO - polish translation
%define rcver	rc1

Summary:	Ksubeditor is a DivX subtitle editor for KDE 3.x.
Summary(pl):	Ksubeditor jest edytorem napis�w dla KDE 3.x.
Name:		ksubeditor
Version:	0.2%{rcver}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://umn.dl.sourceforge.net/sourceforge/sourceforge/ksubeditor/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/ksubeditor/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksubeditor is a DivX subtitle editor for KDE 3.x. It is able to edit
and convert subtitles between different subtitle formats. It is able
to easily change the time of the subtitle and fit it to the movie.

%description -l pl
Ksubeditor jest edytorem napis�w dla KDE 3.x. Jest w stanie edytowa�
oraz konwertowa� napisy pomi�dzy r�nymi formatami. Mo�e w prosty
spos�b zmienia� czas napis�w oraz dopasowa� je do filmu.

%prep
%setup -q

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,\
%{_pixmapsdir}/{locolor/16x16,locolor/32x32},%{_bindir}}

install ksubeditor/lo16-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16
install ksubeditor/lo32-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/32x32
install ksubeditor/ksubeditor $RPM_BUILD_ROOT%{_bindir}
install ksubeditor/ksubeditor.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO AUTHORS COPYING
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/locolor/16x16/*
%{_pixmapsdir}/locolor/32x32/*
%{_applnkdir}/Utilities/ksubeditor.desktop