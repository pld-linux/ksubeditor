Summary:	Ksubeditor - a DivX subtitle editor for KDE 3.x
Summary(pl):	Ksubeditor - edytor napisów dla KDE 3.x
Name:		ksubeditor
Version:	0.13
Epoch:		1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-c++.patch
Patch1:		%{name}-docs.patch	
# Source0-md5:	0849556d80e19ad3ce72909333aa584a
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
Ksubeditor jest edytorem napisów dla KDE 3.x. Jest w stanie
modyfikowaæ oraz konwertowaæ napisy pomiêdzy ró¿nymi formatami. Mo¿e w
prosty sposób zmieniaæ czas napisów oraz dopasowaæ je do filmu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir} 

mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/ksubeditor.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}
echo "Categories=Qt;KDE;Utility;X-KDE-More" >> $RPM_BUILD_ROOT%{_desktopdir}/ksubeditor.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ksubeditor
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/ksubeditor.desktop
