%define upstream_name    Locale-Maketext
%define upstream_version 1.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Framework for software localization
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(I18N::LangTags)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
It is a common feature of applications (whether run directly, or via the
Web) for them to be "localized" -- i.e., for them to a present an English
interface to an English-speaker, a German interface to a German-speaker,
and so on for all languages it's programmed with. Locale::Maketext is a
framework for software localization; it provides you with the tools for
organizing and accessing the bits of text and text-processing code that you
need for producing localized applications.

In order to make sense of Maketext and how all its components fit together,
you should probably go read Locale::Maketext::TPJ13, and _then_ read the
following documentation.

You may also want to read over the source for 'File::Findgrep' and its
constituent modules -- they are a complete (if small) example application
that uses Maketext.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*

