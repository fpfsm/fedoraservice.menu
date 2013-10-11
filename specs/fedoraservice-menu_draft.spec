Name:           fedoraservices.menu
Version:        1.0
Release:        10%{?dist}
Summary:        Catogorized Fedora Services menu for GNOME/KDE menu
Group:		User Interface/Desktops
License:        GPLv2+
URL:            https://github.com/fpfsm/fedoraservice.menu

# No building requires and URL can be change
Source0:        %{name}-%{version}.tar.gz
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:       redhat-menus hicolor-icon-theme
Provides:       dribble-menus = 1.2
Obsoletes:      dribble-menus <= 1.2

%description
Catagorized submenus for the GNOME/KDE Fedora Services menu, for easy to access Fedora Services from shortcut list. 
These icons are just providing launcher icons, none of them running the apps locally, or install it for you. These are
making to you easy access from one structured place, and opens website contents in your default browser.

%prep
#%setup -q


%build
# Nothing to build , only data

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/fedora-icons
#mkdir -p $RPM_BUILD_ROOT${_datadir}/icons/fedora*
install -p -m 644 Fedora.menu \
	$RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
cp -a desktop-directories $RPM_BUILD_ROOT%{_datadir}
#install -p -m desktop-directories \
#	$RPM_BUILD_ROOT%{_datadir}
cp -a icons/* $RPM_BUILD_ROOT%{_datadir}/icons/
#install -p -m 644 icons/* \
#	$RPM_BUILD_ROOT%{_datadir}/icons/

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/fedoraservices || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/fedoraservices || :
fi

%postun
touch --no-create %{_datadir}/icons/fedora-icons || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/fedoraservices || :
fi

%files
%defattr(-,root,root,-)
### document needed %doc COPYING* README
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/Fedora.menu
%{_datadir}/desktop-directories/*.directory
## icon part needed


%changelog
* Tue Oct  8 2013 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.1-1
- Initial release
