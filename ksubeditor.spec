Summary:	Ksubeditor - a DivX subtitle editor for KDE 3.x
Summary(pl):	Ksubeditor - edytor napis�w dla KDE 3.x
Name:		ksubeditor
Version:	0.2
Epoch:		1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ksubeditor/%{name}-%{version}.tar.gz
# Source0-md5:	ddfb1c2ad888127835df09e5479b438d
URL:		http://www.sourceforge.net/projects/ksubeditor/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksubeditor is a DivX subtitle editor for KDE 3.x. It is able to edit
and convert subtitles between different subtitle formats. It is able
to easily change the time of the subtitle and fit it to the movie.

%description -l pl
Ksubeditor jest edytorem napis�w dla KDE 3.x. Jest w stanie
modyfikowa� oraz konwertowa� napisy pomi�dzy r�nymi formatami. Mo�e w
prosty spos�b zmienia� czas napis�w oraz dopasowa� je do filmu.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_desktopdir} 

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/{lo,hi}color
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Applications/ksubeditor.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}
echo "Categories=Qt;KDE;Utility;X-KDE-More;" >> $RPM_BUILD_ROOT%{_desktopdir}/ksubeditor.desktop

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ksubeditor
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/ksubeditor.desktop
